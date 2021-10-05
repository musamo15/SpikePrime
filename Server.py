import pika, os
import json
from pika import connection
from pika.exchange_type import ExchangeType

class Server:
    def __init__(self):
        # Access the CLODUAMQP_URL environment variable and parse it
        url = os.environ.get('CLOUDAMQP_URL', 'amqps://zciavoja:srnFVWWZtZ-m6hH6OK42-e7H0qo66ZPV@clam.rmq.cloudamqp.com/zciavoja')
        params = pika.URLParameters(url)
        self.connection = pika.BlockingConnection(params)
        self.messageChannel = self.connection.channel()

        self.messageChannel.exchange_declare(exchange="test_exchange",
                         passive=False,
                         durable=True,
                         auto_delete=False)
        
        # Set up a queue to request infromation from the simulation
        self.requestQueue = self.messageChannel.queue_declare(queue="Request")
        # Set up a queue for actions within the simulation
        self.actionQueue = self.messageChannel.queue_declare(queue="Action")
        #self.messageChannel.queue_bind(self.actionQueue,exchange="AMQP default",routing_key="Action")
        """
        for item in self.messageChannel.consumer_tags():
            print(item)    
        """
    def sendMessage(self,queue,message):
        print("Attempting to send message")
        try:
            self.messageChannel.basic_publish(exchange='test_exchange',
                  routing_key="Action",
                  body=json.dumps(message))
        except:
            print("Failed to send message on queue " + queue)
    
    def shutDown(self):
        self.connection.close()

if __name__ == "__main__":

    server = Server()
    
    data = {
        "posX": "5",
        "posY": "5"
    }
    currentX = 1
    currentY = 1

    while True:
        data["posX"] = currentX
        data["posY"] = currentY
        server.sendMessage(server.actionQueue,data)
        currentX = currentX + .001
        currentY = currentY + .001

