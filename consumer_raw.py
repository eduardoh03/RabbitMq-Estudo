import pika


def minha_callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


connection = (pika.BlockingConnection
              (pika.ConnectionParameters(host='localhost', port=5672,
                                         credentials=pika.PlainCredentials
                                         ('guest', 'guest'))))
channel = connection.channel()

channel.queue_declare(queue='data_queue', durable=True)

channel.basic_consume(queue='data_queue', on_message_callback=minha_callback, auto_ack=True)
print('Listen RabbitMq on Port 5672')
channel.start_consuming()
