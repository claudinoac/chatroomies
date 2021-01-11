from django.contrib.auth.models import User
from django.db import models  # noqa


class Chatroom(models.Model):
    name = models.CharField(max_length=100)
    active_users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name
