from spike import Singleton

class ColorSensor:

    def __init__(self):
        self.curentColor = None

        self.singleTon = Singleton.getInstance()

    def getColor(self):
        colorDict = self.singleTon.getTranslator().getMessage("color")
        messageColor = colorDict["currentColor"]
        """
        {
            {
                "type" : "color"
                "currentColor": "value"
            }
        }
        """
        if self.curentColor != messageColor:
            self.curentColor = messageColor
        return self.curentColor

 
