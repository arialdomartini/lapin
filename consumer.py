import pika
import json
import sys

host = sys.argv[1]
command = "show"
filter = "True"

if len(sys.argv)> 2:
    filter = sys.argv[2]

if len(sys.argv)> 3:
    command = sys.argv[3]


print("Connecting to %s" % host)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
channel = connection.channel()



def consume_message():
    method_frame, properties, body = channel.basic_get('hello')
    if method_frame:
        # Display the message parts
        #dprint method_frame
        #print properties
        #print body

        m = json.loads(body)
        result = eval( filter )
        if result:
            if command == "show":
                print body
            if command == "delete":
                print "Deleting: %s" % body
                channel.basic_ack(method_frame.delivery_tag)
        return True
    else:
        return False
    
    #channel.basic_ack(method_frame.delivery_tag)

    # Escape out of the loop after 10 messages
    #if method_frame.delivery_tag == 10:
    #    break


while consume_message():
    pass

    
# Cancel the consumer and return any pending messages
channel.cancel()


# Close the channel and the connection
channel.close()
connection.close()
