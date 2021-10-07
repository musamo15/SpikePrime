from spike import Singleton

class ColorSensor:

    #Color Values: black, violet, blue, cyan, green, yellow, red, white, NONE
    validColors = ["black","violet","blue","cyan","green","yellow","red","white","None"]
    def __init__(self):
        self.curentColor = None
        self.light1Brightness = 0
        self.light2Brightness = 0
        self.light3Brightness = 0

        self.singleTon = Singleton.getInstance()

    def get_color(self):
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

    def get_ambient_light(self):
        #get intensity of ambient light as percentage from 0% (dark) - 100% (bright)
        return ambientLight

    def get_reflected_light(self):
        #get intensity of reflected light as pecentage from 0% - 100%
        return reflectedLight

    def get_rgb_intensity(self):
        #get overall color intensity and intensity of r,g,b
        return rgbIntensity

    def get_red(self):
        #redValue = red int of current color
        return redValue

    def get_green(self):
        #greenValue = green int of current color
        return greenValue

    def get_blue(self):
        #blueValue = blue int of current color
        return blueValue

    #wait until specified color is detected
    def wait_until_color(self, color):
        if isinstance(color, str):
            if color not in self.validColors: 
                detected = bool
                while self.get_color() != color:
                    detected = False
            else:
                raise Exception("Color entered is not a valid color")
        else:
            raise Exception("TypeError, color entered is not a String or NONE")
        return detected
            
    def wait_for_new_color(self):
        originalColor = self.getColor()
        newColor = bool
        while self.getColor() == originalColor:
            newColor = False
        return newColor

    #lights up all lights on color sensor at specified brightness
    #brightness = 0 for all lights off
    def light_up_all(self, brightness):
        self.light_up(brightness,brightness,brightness)

    #sets brightness of individual lights on the color sensor at specified brightness
    def light_up(self, light1, light2, light3):
        self.light1Brightness() = light1
        self.light2Brightness() = light2
        self.light3Brightness() = light3
 
