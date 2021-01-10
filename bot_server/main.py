from kombu.mixins import ConsumerProducerMixin
from kombu import Connection, Queue, Consumer, Exchange
from os import environ
from stock import StockQuoteHandler, CommandError
import logging

ROUTING_KEY = environ.get("COMMAND_ROUTING_KEY", "chatroomies.commands")
EXCHANGE = environ.get("EXCHANGE", "chatroomies")
exchange = Exchange(EXCHANGE, type="direct")
main_queue = Queue("bot-server", routing_key=ROUTING_KEY, exchange=Exchange)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

supported_handlers = {
    "stock": StockQuoteHandler(),
}

class Worker(ConsumerProducerMixin):

    def __init__(self, connection, queue):
        self.connection = connection
        self.queue = queue

    def get_consumers(self, consumer, channel):
        return [consumer(
            queues=[self.queue],
            on_message=self.handle_message,
            accept={'application/json'},
            prefetch_count=1
        )]

    def handle_message(self, message):
        command = message.payload.get("command")
        argument = message.payload.get("argument")
        user_id = message.payload.get("user")
        chatroom_id = message.payload.get("chatroom")

        if command in supported_handlers:
            command_handler = supported_handlers.get(command)
            try:
                result = command_handler.handle(argument)
            except CommandError as command_error:
                result = str(command_error)
        else:
            result = f"I don't recognize this command: {command}. Please, try another one"

        logger.info("Result: %s", result)

        self.producer.publish(
            {
                "result": result,
                "user_id": user_id,
                "chatroom_id": chatroom_id,
             },
            exchange="chatroomies",
            routing_key="chatroomies.replies",
            serializer="json",
            retry=True
        )
        message.ack()


if __name__ == '__main__':
    logger.info("Starting server")
    with Connection("amqp://guest:guest@rabbitmq:5672//") as connection:
        try:
            worker = Worker(connection, main_queue)
            worker.run()
        except KeyboardInterrupt:
            print("Tearing down server.")
