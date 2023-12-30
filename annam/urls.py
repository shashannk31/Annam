"""annam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    #authentication
    path('', views.signin, name="signin"),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutview, name="logout"),

    #restaurant
    path('restaurant/home/', views.restauranthome, name="restauranthome"),
    path('restaurant/donate/', views.donate, name="donate"),
    path('restaurant/donatefood/', views.donatefood, name="donatefood"),
    path('restaurant/mycontributions/', views.restaurantmycontributions, name="restaurantmycontributions"),
    path('restaurant/myinbox/', views.restaurantmyinbox, name="restaurantmyinbox"),
    path('restaurant/acceptrejectorder/', views.acceptrejectorder, name="acceptrejectorder"),

    #charity
    path('charity/home/', views.charityhome, name="charityhome"),
    path('charity/order/', views.order, name="order"),
    path('charity/orderfood/', views.orderfood, name="orderfood"),
    path('charity/myorders/', views.charitymyorders, name="charitymyorders"),
    path('charity/myinbox/', views.charitymyinbox, name="charitymyinbox"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
