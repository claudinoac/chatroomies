from apps.message.models import Message


class CreateMessageHandler:

    def handle(self, command):
        return Message.objects.create(
            owner_id=command.user_id,
            content=command.content,
            chatroom_id=command.chatroom_id
        )

