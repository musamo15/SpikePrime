from Translator import translator
class Singleton:
   __instance = None

   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
      
      self.translator = translator()
    
   def getTranslator(self):
        return self.translator
     
class PrimeHub:
    
    def __init__(self):
        # Create Sensors
        print("Created Prime Hub")
        self.singleTon = Singleton.getInstance()