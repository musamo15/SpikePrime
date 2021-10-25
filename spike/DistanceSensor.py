from .Translator import Translator
from .PrimeHub import PrimeHub

class DistanceSensor:

    def __init__(self,id):
        
        self.__primehub = PrimeHub.getInstance()
        self.__translator = Translator.getInstance()
        self.__id = id
        self.__unit = "cm"
        self.__distance = 0.0
        self.__brightness1 = 0
        self.__brightness2 = 0
        self.__brightness3 = 0

    def __get_id(self):
        return self.__id

    #Gets distance from Unity via JSON data
    def __get_distance(self):
        distDict = self.__translator.getMessage("distance")
        messageDict = distDict["value"]
        

        if self.__distance != messageDict:
            self.__distance = messageDict
        return self.__distance

    def __get_unit(self):
        return self.__unit

    #Lights up all distance sensor lights at one brightness
    def light_up_all(self, brightness=100):
        if isinstance(brightness, int):
            self.light_up(brightness)
        else:
            raise Exception("TypeError, brightness is not an int")

    #Specify what brightness each light on distance sensor is set to
    #light_up(right_top, left_top, right_bottom)
    # ***no error checking for 0 <= bightness <= 100****
    def light_up(self, right_top, left_top, right_bottom):
        if isinstance(right_top, int):
            if isinstance(left_top, int):
                if isinstance(right_bottom, int):
                    self.__brightness1 = right_top
                    self.__brightness2 = left_top
                    self.__brightness3 = right_bottom        
                else:
                    raise Exception("TypeError, right_bottom is not an int")
            else:
                raise Exception("TypeException, left_top is not an int")
        else:
            raise Exception("TypeException, right_bottom")

    #Retrieves measured distance in centimeters
    def get_distance_cm(self, short_range=False):
        if isinstance(short_range, bool):
            return float(self.__get_distance())
        else:
            raise Exception("TypeError, short_range is not a string")

    #Retrieves measured distance in inches
    def get_distance_inches(self, short_range=False):
        pass

    #Retrieves measured distance as a percentage 
    def get_distance_percentage(self, short_range=False):
        pass

    #Waits until measured distance is farther than specified distance
    def wait_for_distance_farther_than(self, distance, unit="cm", short_range=False):
        pass 
    
    #Waits until measure distance is closer than specfied distance
    def wait_for_distance_closer_than(self, distance, unit="cm", short_range=False):
        pass