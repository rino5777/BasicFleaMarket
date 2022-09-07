from django.db import models

# Create your models here.



# class Online(models.Model):
#     name = models.CharField(max_length = 100, db_index=True)
    
#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "online"
#         verbose_name_plural = "onlines"


# class ChatModel(models.Model):
#     room_no = models.CharField(max_length = 128)
#     message = models.TextField()
    
#     def __str__(self):
#         return self.name



# from django.contrib.auth.models import User
from user_profile.models import  User
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)