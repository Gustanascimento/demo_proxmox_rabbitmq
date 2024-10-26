import pika

class RabbitMQProducer:
    def __init__(self, queue_name):
        self.host = "192.168.100.23"
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def send_message(self, message):
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=message)
        print(f" [x] Sent {message}")

    def close_connection(self):
        self.connection.close()

if __name__ == "__main__":
    queue_name = 'test_queue'
    producer = RabbitMQProducer(queue_name)
    
    while True:
        mensagem = input("\nDigite a mensagem ou pressione enter para sair: ")
        
        if len(mensagem.strip()) == 0:
            break
        producer.send_message(mensagem)
    producer.close_connection()
    