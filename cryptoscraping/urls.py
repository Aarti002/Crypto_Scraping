"""cryptoscraping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from cryptoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('under_ath_range',views.under_ath_range,name="under_ath_range"),
    path('under_atl_range',views.under_atl_range,name="under_atl_range"),
    path('register_user',views.register_user,name="register_user"),
    path('save_register_user',views.save_register_user,name="save_register_user"),
    path('verify_user/<str:id>',views.verify_user,name="verify_user"),
    path('update_profile_details',views.update_profile_details,name="update_profile_details"),
]
