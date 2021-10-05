from Subscriber import Subscriber
import json
class ColorSensor:

    def __init__(self,id):
        self.id = id
        self.curentColor = None
        subscriber = Subscriber("Test","tcp://localhost:5556")
        

    def getColor(self):
        return self.curentColor

    def setColor(self,message):
        jsonDict = json.loads(message)
        newColor = jsonDict["newColor"]
        if self.curentColor != newColor:
            self.curentColor = newColor

if __name__ == "__main__":

    colorSensor = ColorSensor(1)

        