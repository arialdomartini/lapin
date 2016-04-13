import pika
import json
import sys

host = sys.argv[1]
print("Connecting to %s" % host)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
channel = connection.channel()
channel.queue_declare(queue='hello')

for i in range(1, 10):
    #message= { "name": i, "value": i, "attribute": "boh"}
    message= { "name": i, "value": i}
    jsonmessage = json.dumps(message, ensure_ascii=False)
    channel.basic_publish(exchange='', routing_key='hello',  body=jsonmessage)
    print " [x] Sent '%r'" % (message)
