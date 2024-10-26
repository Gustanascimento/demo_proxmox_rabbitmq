import pika


class RabbitMQProducer:
    def __init__(self, queue_name):
        self.host = "192.168.100.23"
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=self.queue_name)
        self.channel.basic_qos(prefetch_count=1)

    def send_message(self, message):
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=message)
        print(f'🐳 Enviou: "{message}"\n')

    def close_connection(self):
        self.connection.close()


if __name__ == "__main__":
    print("🚀 Iniciando o produtor de mensagens 🚀\n\n")
    
    queue_name = 'test_queue'
    producer = RabbitMQProducer(queue_name)
    
    while True:
        mensagem = input("👉 Digite uma mensagem ou pressione enter para sair: ")
        
        if len(mensagem.strip()) == 0:
            break
        producer.send_message(mensagem)
    producer.close_connection()
    