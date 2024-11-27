"""
URL configuration for bike project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from GT650.views import *
from KTM.views import *
from R15.views import *
from TVSXL.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('GT650/',include('GT650.urls')),
    path('KTM/',include('KTM.urls')),
    path('R15/',R15,name='R15'),
    path('TVSXL/',TVSXL,name='TVSXL'),
      
]
