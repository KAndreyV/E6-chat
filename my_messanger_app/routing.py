from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path, path
from my_messanger_app import consumers

# URLs that handle the WebSocket connection are placed here.
websockets = URLRouter([
                    path(
                        "ws/chat/(?P<chat_box_name>[A-Za-z0-9_-]+)", consumers.ChatRoomConsumer.as_asgi()
                    ),
                ])