import pika

def callback(ch, method, properties, body):
    print("Received msg: " + body.decode("utf-8"))


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume('hello',
  callback,
  auto_ack=True)

channel.start_consuming()
    

