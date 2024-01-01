from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, LoginForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import FoodOrder

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['username']=user.username
            request.session['organization_type']=user.organization_type
            request.session['organization_name']=user.organization_name
            request.session['city']=user.city
            request.session['state']=user.state
            request.session['address']=user.address
            request.session['phone']=user.phone
            request.session['cuisine_type']=user.cuisine_type
            request.session['email']=user.email
            login(request, user,backend='app.auth_backends.CustomUserModelBackend')
            if request.session.get('organization_type') == "Restaurant":
                return redirect('restauranthome')
            elif request.session.get('organization_type') == "Old Age Home" or request.session.get('organization_type') == "Orphanage":
                return redirect('charityhome')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})


def signin(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        #print(form)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #print(email)
            #print(password)
            user = authenticate(request, email=email, password=password)
            #print(user)
            if user is not None:
                login(request, user,backend='app.auth_backends.CustomUserModelBackend')
                request.session['username']=user.username
                request.session['organization_type']=user.organization_type
                request.session['organization_name']=user.organization_name
                request.session['city']=user.city
                request.session['state']=user.state
                request.session['address']=user.address
                request.session['phone']=user.phone
                request.session['cuisine_type']=user.cuisine_type
                request.session['email']=user.email
                if request.session.get('organization_type') == "Restaurant":
                    return redirect('restauranthome')
                elif request.session.get('organization_type') == "Old Age Home" or request.session.get('organization_type') == "Orphanage":
                    return redirect('charityhome')
            else:
                messages.error(request, 'Invalid credentials. Please try again!')
    return render(request, 'app/signin.html', {'form': form})

def logoutview(request):
    logout(request)
    return redirect('signin')




#Restaurant
def restauranthome(request):
    username=request.session.get('username')
    print(username)
    return render(request, 'app/restauranthome.html', {'username': username})

def donate(request):
    username=request.session.get('username')
    return render(request, 'app/donatefood.html', {"username":username})

def donatefood(request):
    username=request.session.get('username')
    if request.method == "POST":
        organization_name=request.session.get('organization_name')
        city=request.session.get('city')
        state=request.session.get('state')
        address=request.session.get('address')
        phone=request.session.get('phone')
        cuisine_type=request.session.get('cuisine_type')
        time_of_preparation = request.POST.get("time_of_preparation")
        name_of_food = request.POST.get("name_of_food")
        food_cuisine = request.POST.get("food_cuisine")
        quantity_serves = request.POST.get("quantity_serves")
        storage_duration = request.POST.get("storage_duration")
        tentative_collection_time = request.POST.get("tentative_collection_time")
        packing_present = request.POST.get("packing_present")

        if time_of_preparation:
            time_of_preparation = timezone.datetime.strptime(time_of_preparation, "%Y-%m-%dT%H:%M")
        if tentative_collection_time:
            tentative_collection_time = timezone.datetime.strptime(tentative_collection_time, "%Y-%m-%dT%H:%M")

        food_order = FoodOrder(
            organization_name=organization_name,
            city=city,
            state=state,
            restaurant_address=address,
            restaurant_phone=phone,
            cuisine_type=cuisine_type,
            time_of_preparation=time_of_preparation,
            name_of_food=name_of_food,
            food_cuisine=food_cuisine,
            quantity_serves=quantity_serves,
            storage_duration=storage_duration,
            tentative_collection_time=tentative_collection_time,
            packing_present=packing_present,
            is_live=True
        )

        food_order.save()
        messages.success(request,'Details Posted Successfully')
    return render(request, 'app/donatefood.html', {"username":username})

def restaurantmycontributions(request):
    username=request.session.get('username')
    restaurant_phone=request.session.get('phone')
    my_contributions=FoodOrder.objects.filter(restaurant_phone=restaurant_phone)
    return render(request, 'app/restaurantmycontributions.html', {"my_contributions":my_contributions, "username":username})

def restaurantmyinbox(request):
    username=request.session.get('username')
    restaurant_phone=request.session.get('phone')
    my_inbox=FoodOrder.objects.filter(restaurant_phone=restaurant_phone)
    return render(request, 'app/restaurantmyinbox.html', {"my_inbox":my_inbox, "username":username})

def acceptrejectorder(request):
    username=request.session.get('username')
    if request.method=="POST":
        response = request.POST.get('response')
        id = request.POST.get('id')
        if response=='accept':
            forder=FoodOrder.objects.get(id=id)
            forder.accept_reject_status=False
            forder.display_status=True
            forder.restaurant_order_status="Accepted"
            forder.charity_inbox=True
            forder.save()
            return redirect('restaurantmyinbox')
        elif response=='reject':
            forder=FoodOrder.objects.get(id=id)
            forder.accept_reject_status=False
            forder.is_live=True
            forder.restaurant_order_status="Rejected"
            forder.charity_inbox=True
            forder.save()
            return redirect('restaurantmyinbox')
    return redirect('restaurantmyinbox')



#Charity
def charityhome(request):
    username=request.session.get('username')
    print(username)
    return render(request, 'app/charityhome.html', {'username': username})

def order(request):
    username=request.session.get('username')
    live_food_items = FoodOrder.objects.filter(is_live=True)
    print(live_food_items)
    return render(request,'app/order.html', {"live_food_items":live_food_items, "username":username})

def orderfood(request):
    username=request.session.get('username')
    if request.method=="POST":
        id = request.POST.get("id")
        name_of_food = request.POST.get("name_of_food")
        organization_name = request.POST.get("organization_name")
        cuisine_type = request.POST.get("cuisine_type")
        quantity_serves = request.POST.get("quantity_serves")
        time_of_preparation = request.POST.get("time_of_preparation")
        tentative_collection_time = request.POST.get("tentative_collection_time")
        restaurant_phone = request.POST.get("restaurant_phone")
        restaurant_address = request.POST.get("restaurant_address")
        food_cuisine = request.POST.get("food_cuisine")
        packing_present = request.POST.get("packing_present")
        delivery_address = request.session.get('address')
        charity_phone = request.session.get('phone')
        charity_name = request.session.get('organization_name')
        existing_instance = FoodOrder.objects.get(id=id)

        existing_instance.order_timestamp = timezone.now()
        existing_instance.delivery_address = delivery_address
        existing_instance.charity_phone = charity_phone
        existing_instance.charity_name = charity_name
        existing_instance.restaurant_inbox = True
        existing_instance.is_live = False
        existing_instance.accept_reject_status = True
        existing_instance.restaurant_order_status = "Nil"

        existing_instance.save()
        messages.success(request,'Food ordered successfully')
        return redirect('order')

    live_food_items = FoodOrder.objects.filter(is_live=True)
    return render(request, 'app/order.html', {"live_food_items": live_food_items, "messages": messages.get_messages(request), "username":username})

def charitymyorders(request):
    username=request.session.get('username')
    charity_phone=request.session.get('phone')
    my_orders=FoodOrder.objects.filter(charity_phone=charity_phone)
    return render(request, 'app/charitymyorders.html', {"my_orders":my_orders, "username":username})

def charitymyinbox(request):
    username=request.session.get('username')
    charity_phone=request.session.get('phone')
    my_inbox=FoodOrder.objects.filter(charity_phone=charity_phone)
    return render(request, 'app/charitymyinbox.html', {"my_inbox":my_inbox, "username":username})
