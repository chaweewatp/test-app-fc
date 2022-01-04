from django.urls import path, include
from . import views

urlpatterns = [

    path('showenv/showall', views.showall, name='showall'),


]