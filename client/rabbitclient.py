import pika
import json
import base64

def callback(ch, method, properties, body):
    
    obj = json.loads(body)
    
    imgbytes = base64.b64decode(obj['image'])
    f = open('image2.jpg', mode='wb')
    f.write(imgbytes)
    f.close()

    print('image received')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
