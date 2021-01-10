from django.db import models
from django.contrib.auth.models import User
from apps.chatroom.models import Chatroom


class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
