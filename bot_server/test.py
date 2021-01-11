from kombu import Connection, Exchange, Queue

task_queue = Queue("bot-server", Exchange("chatroomies"), routing_key="chatroomies.commands")
connection = Connection("amqp://guest:guest@rabbitmq:5672//")
connection.connect()
producer = connection.Producer()
producer.publish(
    {"command": "stock", "argument": "googl.us", "user_id": 10, "chatroom_id": 1},
    retry=True,
    exchange=task_queue.exchange,
    routing_key=task_queue.routing_key,
    declare=[task_queue],
)
