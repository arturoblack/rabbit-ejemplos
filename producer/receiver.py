#!/usr/bin/env python
import pika, sys, os
import time;
import json 

def main():
    parameters = pika.URLParameters('amqp://guest:guest@localhost:5672')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='ejemplo')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        j = json.loads(body)
        if(1):
            if 'times' in j:
                j['times'] = int(j['times']) + 1
            else : j['times'] = 1
            if (j['times'] < 5):
                newbody = json.dumps(j)
                channel.basic_publish(exchange='',
                        routing_key='ejemplo',
                        body=newbody)
            else:
                newbody = json.dumps(j)
                channel.basic_publish(exchange='',
                        routing_key='ejemplo-errores',
                        body=newbody)
        time.sleep(1)

    channel.basic_consume(queue='ejemplo', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)