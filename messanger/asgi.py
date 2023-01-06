from channels.routing import ProtocolTypeRouter, URLRouter
import os
from django.core.asgi import get_asgi_application
import my_messanger_app.routing #new
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messanger.settings')

asgi_application = get_asgi_application() #new



application = ProtocolTypeRouter({
            "http": asgi_application,
            "websocket": AllowedHostsOriginValidator(AuthMiddlewareStack(
            URLRouter(my_messanger_app.routing.websocket_urlpatterns)
                ),
            )
})