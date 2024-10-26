import pika
from time import sleep
from datetime import datetime

class RabbitMQConsumer:
    def __init__(self, queue_name: str):
        self.queue_name = queue_name
        self.host = "192.168.100.23"
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def run_consumer(self):
        print(f'📡 Aguardando mensagens na fila "{self.queue_name}"...\n')
        
        for method, properties, body in self.channel.consume(self.queue_name):
            message = body.decode()
            print(f" ✅ Mensagem processada às {datetime.now().strftime('%H:%M:%S')}: {message}")
            self.channel.basic_ack(method.delivery_tag)
            sleep(4)

if __name__ == "__main__":
    consumer = RabbitMQConsumer(queue_name='test_queue')
    consumer.run_consumer()