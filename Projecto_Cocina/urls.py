"""Projecto_Cocina URL Configuration

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
from django.urls import path
from Recetas.views import (index, MundoRecetasList, MundoRecetasDetail, MundoRecetasUpdate, MundoRecetasCreate,
    MundoRecetasDelete, MundoRecetasSearch
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , index , name='recetas'),
    path('recetas/list', MundoRecetasList.as_view(), name='recetas-list'),
    path('recetas/detail/<pk>', MundoRecetasDetail.as_view(), name='recetas-detail'),
    path('recetas/update/<pk>', MundoRecetasUpdate.as_view(), name='recetas-update'),
    path('recetas/delete/<pk>', MundoRecetasDelete.as_view(), name='recetas-delete'),
    path('recetas/create', MundoRecetasCreate.as_view(), name='recetas-create'),
    path('recetas/search', MundoRecetasSearch.as_view(), name='recetas-search')
]
    