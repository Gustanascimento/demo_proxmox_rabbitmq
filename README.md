# RabbitMQ Docker Compose Project

This project demonstrates how to set up a RabbitMQ message broker along with producer and consumer Python scripts using Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Gustanascimento/demo_proxmox_rabbitmq
    cd demo_proxmox_rabbitmq
    ```

2. **Build and start the services:**
    ```sh
    docker-compose up --build
    ```

3. **Verify the setup:**
    - RabbitMQ management interface should be accessible at `http://localhost:15672`
    - Default username and password are `guest`/`guest`

## Project Structure

- `docker-compose.yml`: Defines the RabbitMQ service.
- `producer.py`: Python script that sends messages to RabbitMQ.
- `consumer.py`: Python script that consumes messages from RabbitMQ.

## Configuration

- RabbitMQ settings can be modified in the `docker-compose.yml` file.
- Producer and consumer configurations can be adjusted in their respective Python scripts.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [RabbitMQ](https://www.rabbitmq.com/)
- [Docker](https://www.docker.com/)
