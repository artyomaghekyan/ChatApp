from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='rooms'),
    path('room/<slug:slug>/', views.chatroom, name='chatroom'),
    path('create', views.create, name='create'),
]