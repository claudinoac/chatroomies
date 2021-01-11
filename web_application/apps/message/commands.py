from dataclasses import dataclass


@dataclass
class CreateMessageCommand:
    user_id: int
    chatroom_id: int
    content: str

@dataclass
class CreateBotMessageCommand:
    user_id: int
    chatroom_id: int
    command: str
    argument: str
