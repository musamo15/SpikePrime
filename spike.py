from MotorPair import MotorPair
from ColorSensor import ColorSensor
from Server import Server

class PrimeHub:
    
    def __init__(self):
        self.id = 1
        # Create Sensors
        self.motorPair = MotorPair()
        self.colorSensor = ColorSensor()

        # Establish Connection With RabbitMQ
        self.server = Server()
       
      
