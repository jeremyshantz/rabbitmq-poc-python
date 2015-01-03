#!/usr/bin/env python

#

import pika
import json
import base64

def callback(ch, method, properties, body):
    payload = base64.b64decode(body)
    print " [x] Received %r" % (body) + ' ' + payload
    obj = json.loads(payload)
    print (obj['test'])

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_consume(callback, queue='hello', no_ack=True)

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()
