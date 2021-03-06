"""cciswebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from cciswebsite import views
from django.conf.urls import url, static
from cciswebsite.settings import MEDIA_ROOT
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('course/<int:id>/',views.blog_content),
    path('notice/<int:id>/',views.notice_content),
    url(r'^media/(?P<path>.*)', static.serve, {"document_root": MEDIA_ROOT}),
]

