from django.contrib.auth.models import User
from django.db import models  # noqa
from django.urls import reverse


class Chatroom(models.Model):
    name = models.CharField(max_length=100)
    active_users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("chatroom:chatroom_view", args=[self.id])
