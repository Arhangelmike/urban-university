"""
URL configuration for UrbanDjango project.

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
from django.views.generic import TemplateView
from task4.views import games, cart, platform, index

urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    # path('games', games.as_view(), name='games'),
    # path('cart', cart.as_view(), name='cart'),
    # path('platform', platform.as_view(), name='platform'),
    path('games', games, name='games'),
    path('cart', cart, name='cart'),
    path('platform', platform, name='platform'),

]
