"""
URL configuration for ictapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from accounts import views
urlpatterns = [
    path('',views.pre_register),
    path('admin/', admin.site.urls),
    path("pre_register",views.pre_register),
    path("otp_verification",views.api_check_otp_view,name="api_check_otp_view"),
    path("update",views.update_data_view,name="update_data"),
    path("login",views.login_view,name="login")
]