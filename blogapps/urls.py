"""blogapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
"""
Notes Written By Aryadrj
1.The quotes are called docstrings
"""

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #This code is for URL path for admin and we can access it by URL/admin
    path('admin/', admin.site.urls),
    #adding blog url and now whenever we will enter  url 127.0.0.. it will direct to blog.url
    path('',include('blog.urls')),
]
