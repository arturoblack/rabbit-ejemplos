#!/usr/bin/env python
import pika
import time

t  = time.time()
parameters = pika.URLParameters('amqp://guest:guest@localhost:5672')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()


channel.queue_declare(queue='ejemplo')
channel.basic_publish(exchange='',
                      routing_key='ejemplo',
                      body='{"name":"holass", "t": '+str(t)+'}')
print(" [x] Sent 'Hello World!'")
connection.close()