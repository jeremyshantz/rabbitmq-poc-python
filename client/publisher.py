#!/usr/bin/env python

#

import pika

VERSION = '0.0.1'

payload = '{"test": "hello, world"}'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body=payload)

print " [x] Sent message"

connection.close()
