import logging
from kombu.mixins import ConsumerMixin
from django.conf import settings
from os import environ
from kombu import Connection, Queue, Consumer, Exchange
from apps.message.commands import CreateMessageCommand
from apps.message.handlers import CreateMessageHandler


exchange = Exchange(settings.EXCHANGE, type="direct")
main_queue = Queue("cmd-receiver", routing_key=settings.ROUTING_KEY, exchange=exchange)


logger = logging.getLogger(__name__)


class BotMessageWorker(ConsumerMixin):

    def __init__(self, connection, queue):
        self.connection = connection
        self.queue = queue

    def get_consumers(self, consumer, channel):
        return [consumer(
            queues=[self.queue],
            callbacks=[self.handle_message],
            accept={'application/json'},
            prefetch_count=1
        )]

    def handle_message(self, body, message):
        result = body.get("result")
        chatroom_id = body.get("chatroom_id")
        logger.info(body)
        command = CreateMessageCommand(
            user_id=settings.BOT_USER_ID,
            content=result,
            chatroom_id=chatroom_id
        )
        CreateMessageHandler().handle(command)
        message.ack()


def start_worker():
    logger.info("Starting bot receiver server")
    with Connection(settings.AMQP_ADDRESS) as connection:
        try:
            worker = BotMessageWorker(connection, main_queue)
            worker.run()
        except KeyboardInterrupt:
            print("Tearing down server.")

