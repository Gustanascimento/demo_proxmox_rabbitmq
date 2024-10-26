import pika

class RabbitMQConsumer:
    def __init__(self, queue_name: str):
        self.queue_name = queue_name
        self.host = "192.168.100.23"
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def run_consumer(self):
        print(f" [*] Waiting for messages in {self.queue_name}. To exit press CTRL+C")
        
        for method, properties, body in self.channel.consume(self.queue_name):
            message: str = body.decode()
            print(f" [x] Message received from queue {self.queue_name}: {message}")
            self.channel.basic_ack(method.delivery_tag)

if __name__ == "__main__":
    consumer = RabbitMQConsumer(queue_name='test_queue')
    consumer.run_consumer()