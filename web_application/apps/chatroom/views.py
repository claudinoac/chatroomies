import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from apps.chatroom.models import Chatroom
from apps.message.commands import CreateMessageCommand
from apps.message.forms import MessageForm
from apps.message.handlers import CreateMessageHandler

logger = logging.getLogger(__name__)


class ChatroomView(LoginRequiredMixin, TemplateView):
    template_name = "chatroom/chatroom_view.html"
    form_class = MessageForm
    handler = CreateMessageHandler()

    def get_context_data(self, chatroom_id, user_id):
        chatroom = get_object_or_404(Chatroom, id=chatroom_id)
        message_list = list(chatroom.message_set.order_by("-created")[:50])
        message_list.reverse()
        context = {
            "chatroom": chatroom,
            "messages": message_list,
            "form": self.form_class(),
        }
        return context

    def get(self, request, chatroom_id):
        context = self.get_context_data(chatroom_id, request.user.id)
        return render(request, self.template_name, context)

    def post(self, request, chatroom_id):
        form = self.form_class(
            {
                "content": request.POST.get("content"),
                "user_id": request.user.id,
                "chatroom_id": chatroom_id,
            }
        )
        if form.is_valid():
            command = CreateMessageCommand(
                user_id=form.cleaned_data.get("user_id"),
                chatroom_id=form.cleaned_data.get("chatroom_id"),
                content=form.cleaned_data.get("content"),
            )
            result = self.handler.handle(command)
            logger.error(result)
        else:
            pass

        context = self.get_context_data(chatroom_id, request.user.id)
        return render(request, self.template_name, context)


def chatroom_add_view(request):
    return HttpResponse("Chatroom with ID {} Added!")
