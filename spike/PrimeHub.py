from .Translator import Translator

class PrimeHub:
    __instance = None
    def __init__(self):
        PrimeHub.__instance = self
        print("Created Prime Hub")
        self.TransLator = Translator.getInstance()
    
    @staticmethod 
    def getInstance():
      """ Static access method. """
      if PrimeHub.__instance == None:
         raise Exception("Theres no hub")
      return PrimeHub.__instance
    