from django.urls import path
from .views import ChatRoom


app_name = 'chat'

urlpatterns = [

    path('chat/', ChatRoom.as_view(),name='main'),
    


]