from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Room, Message
# Create your views here.
class ChatRoom(TemplateView):
    template_name = 'chat/room.html'
    
    def get(self, request, *args, **kwargs):
       
        
        self.room = Room.objects.get()
        self.messages = Message.objects.filter(room=self.room)[0:25]
        
        return super().get(request, *args, **kwargs)
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = self.room
        
        context['messages'] = self.messages
      
        return context







