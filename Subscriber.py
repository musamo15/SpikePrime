#!/usr/bin/python3
import zmq
import threading
import time
class Subscriber():

    def __init__(self,topics,host):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect(host)

        # Set the topics 
        for topic in topics:
            self.socket.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))
        subscriber_thread = threading.Thread(target=self.subscribe, name="subscriber_thread")
        subscriber_thread.start()
        print("After Thread")
    
    def subscribe(self):
        try:
            while True:
                print("Subscriber")
                topic, msg = self.socket.recv_multipart()
                print('   Topic: %s, msg:%s' % (topic.decode('utf-8'), msg.decode('utf-8')))
        except KeyboardInterrupt:
            print("Stopped Subscribing")

subscriber = Subscriber("Test","tcp://localhost:5556")
        