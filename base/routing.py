from django.urls import path

from .import consumrs

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumrs.ChatConsumer.as_asgi()),
    
]