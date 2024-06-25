from channels.generic.websocket import WebsocketConsumer  # Importa la clase WebsocketConsumer de Channels.
import json  # Importa el módulo json para manejar datos en formato JSON.
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    # Clase que maneja la conexión WebSocket para el chat.
    
    def connect(self):
        # Método que se llama cuando se establece una nueva conexión WebSocket.
        
        self.room_group_name = 'test'
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        ) 
        
        self.accept()  # Acepta la conexión WebSocket.
        
        # Envía un mensaje de confirmación al cliente indicando que la conexión ha sido establecida.
        self.send(text_data=json.dumps({
            'type':'connection',  # Tipo de mensaje.
            'message':'You are connected'  # Contenido del mensaje.
        }))            

    def disconnect(self, close_code):
        # Método que se llama cuando la conexión WebSocket se cierra.
        pass  # No hace nada en este ejemplo.

    def receive(self, text_data):
        # Método que se llama cuando se recibe un mensaje a través de la conexión WebSocket.
        
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        ) 
        
        # self.send(text_data=json.dumps({
        #     'type': 'chat',
        #     'message': message
        # }))  # Reenvía el mismo mensaje recibido de vuelta al cliente.

    def chat_message(self, event):
        message = event['message']
        
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))