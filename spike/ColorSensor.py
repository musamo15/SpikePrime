from .Translator import Translator
from .PrimeHub import PrimeHub

"""
    This library represents the color sensor of the spike prime library
"""
class ColorSensor:

    def __init__(self,id):
        PrimeHub.getInstance()
        self.id = id
        self.__curentColor = None
        self.__translator = Translator.getInstance()
        self.__rgbDict = {
            "Black":(0,0,0),
            "White":(255,255,255),
            "Blue":(0,0,255),
            "Green":(11,53,11),
            "Light Blue":(0,191,255),
            "Light Green": (0,255,0),
            "Orange":(255,165,0),
            "Pink":(255,192,203),
            "Red":(255,0,0),
            "Violet":(138,43,226),
            "Yellow":(255,255,0)            
        }
    """
        Retrieves the currrent color detected by the simulation on that respective port
    """
    def get_color(self):
        messageDict = {
            "messageType": "color",
            "messageRequestType":"Request",
            "id": self.id
        }
        colorDict = self.__translator.getMessageFromUnity(messageDict)
        if colorDict == None:
            return None
        else:
            messageColor = colorDict["currentColor"]
            if self.__curentColor != messageColor:
                self.__curentColor = messageColor
            return self.__curentColor

    """
        Returns the reflected light detected by the simulation.
        Returns 100 if the detected color is white, 0 if its black
    """
    def get_reflected_light(self):     
        return self.__getRGBValue(str(self.get_color()).strip())
 
    def __getRGBValue(self,color):
        try:
            rgbValue = self.__rgbDict[color]
        except KeyError:
            return 0
        total = 0
        for color in rgbValue:
            total += color
        value = (total / 3) * (100/255)
        return int(value)
        
        
    
    """
        The following methods are currently not implemented.
    def get_ambient_light(self):
        #get intensity of ambient light as percentage from 0% (dark) - 100% (bright)
        pass
        
    def get_rgb_intensity(self):
        #get overall color intensity and intensity of r,g,b
        pass

    def get_red(self):
        #redValue = red int of current color
        pass

    def get_green(self):
        #greenValue = green int of current color
        pass

    def get_blue(self):
        #blueValue = blue int of current color
        pass

    #Wait until specified color is detected
    def wait_until_color(self, color):
        if isinstance(color, str):
            validColors = ["black","violet","blue","cyan","green","yellow","red","white","None"]
            if color in validColors:
                currentColor =  self.get_color()
                while currentColor != color:
                     currentColor =  self.get_color()
            else:
                raise Exception("Color entered is not a valid color")
        else:
            raise Exception("TypeError, color entered is not a String or NONE")
    
    #Wait for color other than current color
    def wait_for_new_color(self):
        originalColor = self.getColor()
        newColor = False
        currentColor = originalColor
        while not newColor:
            currentColor = self.getColor()
            if currentColor!= originalColor:
                newColor = True

        return currentColor

    #Lights up all lights on color sensor at specified brightness
    #brightness = 0 for all lights off
    def light_up_all(self, brightness=100):
        self.__light_up(brightness,brightness,brightness)

    #Sets brightness of individual lights on the color sensor at specified brightness
    def __light_up(self, firstLight, secondLight, thirdLight):
        self.__light1Brightness = firstLight
        self.__light2Brightness = secondLight
        self.__light3Brightness = thirdLightcd 
    """
    
 
