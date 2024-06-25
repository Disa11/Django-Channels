from django.urls import re_path  # Importa la función re_path para definir rutas usando expresiones regulares.
from . import consumers  # Importa el módulo consumers del paquete actual.

# Define una lista de patrones de URL para las conexiones WebSocket.
websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),  # Define una ruta WebSocket que utiliza ChatConsumer.
]
