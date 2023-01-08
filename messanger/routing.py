from channels.routing import ProtocolTypeRouter, URLRouter
from messanger.my_messanger_app.routing import websockets


application = ProtocolTypeRouter(
    {
        "websocket": websockets,
    }
)


