from django.contrib import admin
from apps.message.models import Message
from apps.chatroom.models import Chatroom


class MessageAdmin(admin.ModelAdmin):
    list_display = ('owner', 'content', 'chatroom', 'created')


admin.site.register(Message, MessageAdmin)
