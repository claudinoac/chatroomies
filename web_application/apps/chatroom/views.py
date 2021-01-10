from django.http import HttpResponse
from apps.chatroom.models import Chatroom
from apps.message.models import Message
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from apps.message.forms import MessageForm
from apps.message.commands import CreateMessageCommand
from apps.message.handlers import CreateMessageHandler

import logging


logger = logging.getLogger(__name__)

class ChatroomView(TemplateView):
    template_name = "chatroom/chatroom_view.html"
    form_class = MessageForm
    handler = CreateMessageHandler()

    def get_context_data(self, chatroom_id, user_id):
        chatroom = get_object_or_404(Chatroom, id=chatroom_id)
        initial_data = {
            "user_id": user_id,
            "chatroom_id": chatroom_id
        }
        context = {
            'chatroom': chatroom,
            'messages': chatroom.message_set.order_by('created')[:50],
            'form': self.form_class(initial=initial_data)
        }
        return context

    def get(self, request, chatroom_id):
        context = self.get_context_data(chatroom_id, request.user.id)
        return render(request, self.template_name, context)

    def post(self, request, chatroom_id):
        context = self.get_context_data(chatroom_id, request.user.id)
        form = self.form_class({
            'content': request.POST.get("content"),
            'user_id': request.user.id,
            'chatroom_id': chatroom_id
        })
        if form.is_valid():
            command = CreateMessageCommand(
                user_id=form.cleaned_data.get("user_id"),
                chatroom_id=form.cleaned_data.get("chatroom_id"),
                content=form.cleaned_data.get("content")
            )
            result = self.handler.handle(command)
            logger.error(result)
        else:
            pass

        return render(request, self.template_name, context)


def chatroom_add_view(request):
    return HttpResponse("Chatroom with ID {} Added!")
