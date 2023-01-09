import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from my_messanger_app.middleware import JwtAuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messanger.settings')
django.setup()

from my_messanger_app import routing
# application = get_asgi_application()

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": JwtAuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})