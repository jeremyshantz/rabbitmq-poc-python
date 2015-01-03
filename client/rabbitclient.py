#!/usr/bin/env python

#

import pika
import json

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    obj = json.load(body)
    print " [x] Received %r" % (obj['test'])

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)


print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()
