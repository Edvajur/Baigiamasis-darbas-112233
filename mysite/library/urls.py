"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from .views import search_view

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.game_list, name='game_list'),
    path('developers/', views.developer_list, name='developer_list'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('games/<int:pk>/', views.game_detail, name='game_detail'),
    path('genres/', views.genre_list, name='genre_list'),
    path('search/', search_view, name='search'),
    # path('search/', views.search_results, name='search_results'),
]
