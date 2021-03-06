#!/usr/bin/env python

#

import pika
import base64

VERSION = '0.0.1'

def buildmessage ():
	f = open('image.jpg', mode='rb')
	bytes = base64.b64encode(bytearray(f.read()))
	f.close()
	payload = '{"test": "hello, world", "image": "' + bytes + '"}'
	return payload


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body=buildmessage())

print(" [x] Sent message")

connection.close()


# public class MessageV2
# {
# 	public string[] To { get; set; }
# 	public string[] CC { get; set; }
# 	public string[] BCC { get; set; }
# 	public string Subject { get; set; }
# 	public string Body { get; set; }
# 	public List<AttachmentV2> Attachments { get; set; }
# }

#  public class AttachmentV2
# {
# 	public string FileName { get; set; }
# 	public string Base64 { get; set; }
# }
