from apps.message.models import Message
from kombu import Connection, Queue, Exchange
from apps.message.commands import CreateBotMessageCommand
from django.conf import settings


class CreateBotMessageHandler:
    def handle(self, command):
        command_body = {
            "command": command.command,
            "argument": command.argument,
            "user_id": command.user_id,
            "chatroom_id": command.chatroom_id
        }
        connection = Connection(settings.AMQP_ADDRESS)
        connection.connect()
        producer = connection.Producer()
        producer.publish(
            command_body,
            retry=True,
            exchange=settings.EXCHANGE,
            routing_key=settings.SENDER_ROUTING_KEY,
        )


class CreateMessageHandler:

    def handle(self, command):
        if command.content.startswith("/"):
            cleaned_message = command.content.split("/")[-1]
            try:
                bot_command, bot_argument = cleaned_message.split("=")
            except ValueError:
                bot_command = cleaned_message
                bot_argument = ""
            new_command = CreateBotMessageCommand(
                command=bot_command,
                argument=bot_argument,
                chatroom_id=command.chatroom_id,
                user_id=command.user_id
            )
            CreateBotMessageHandler().handle(new_command)

        return Message.objects.create(
            owner_id=command.user_id,
            content=command.content,
            chatroom_id=command.chatroom_id
        )
