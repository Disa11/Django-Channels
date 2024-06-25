"""
ASGI config for DjangoChat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
import os  # Importa el módulo 'os' para interactuar con el sistema operativo.
from django.core.asgi import get_asgi_application  # Importa la función para obtener la aplicación ASGI de Django.
from channels.routing import ProtocolTypeRouter, URLRouter  # Importa los routers para manejar diferentes tipos de protocolos.
from channels.auth import AuthMiddlewareStack  # Importa el middleware de autenticación para manejar las conexiones WebSocket autenticadas.
import chat.routing  # Importa el módulo de enrutamiento de la aplicación 'chat'.

# Establece la configuración predeterminada de Django para el proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoChat.settings')

# Define la aplicación ASGI que manejará las conexiones HTTP y WebSocket.
application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # Usa la aplicación ASGI de Django para manejar solicitudes HTTP.
    
    'websocket': AuthMiddlewareStack(  # Usa el AuthMiddlewareStack para manejar WebSockets autenticados.
        URLRouter(
            chat.routing.websocket_urlpatterns  # Define las rutas de WebSocket usando las URL definidas en 'chat.routing'.
        )
    ),
})