from .Translator import Translator
from .PrimeHub import PrimeHub

class ColorSensor:

    validColors = ["black","violet","blue","cyan","green","yellow","red","white","None"]
    def __init__(self,id):
        self.primeHub = PrimeHub.getInstance()
        self.curentColor = None
        self.light1Brightness = 0
        self.light2Brightness = 0
        self.light3Brightness = 0

        self.translator = Translator.getInstance()

    #Gets current color from Unity via JSON data
    def get_color(self):
        colorDict = self.translator.getMessage("color")
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

    def get_ambient_light(self):
        #get intensity of ambient light as percentage from 0% (dark) - 100% (bright)
        pass

    def get_reflected_light(self):
        #get intensity of reflected light as pecentage from 0% - 100%
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
            if color not in self.validColors: 
                while self.get_color() != color:
                    detected = False

                detected = True
            else:
                raise Exception("Color entered is not a valid color")
        else:
            raise Exception("TypeError, color entered is not a String or NONE")
        return detected
    
    #Wait for color other than current color
    def wait_for_new_color(self):
        originalColor = self.getColor()
        newColor = bool
        while self.getColor() == originalColor:
            newColor = False
        return newColor

    #Lights up all lights on color sensor at specified brightness
    #brightness = 0 for all lights off
    def light_up_all(self, brightness):
        self.light_up(brightness,brightness,brightness)

    #Sets brightness of individual lights on the color sensor at specified brightness
    def light_up(self, light1, light2, light3):
        self.light1Brightness = light1
        self.light2Brightness = light2
        self.light3Brightness = light3
 
