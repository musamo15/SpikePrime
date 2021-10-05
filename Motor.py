class Motor:

    def __init__(self,id,speed,rotation,stopAction):
        self.id = id
        self.speed = speed
        self.rotation = rotation
        self.stopAction = stopAction
        self.unit = "cm"
        self.currentMessageDict = {}
    def setRotation(self,rotation,unit):
        if self.rotation != rotation:
            self.rotation = rotation
        if self.unit != unit:
            self.unit = unit
    def setSpeed(self,newSpeed):
        if isinstance(newSpeed,int):
            if self.speed != newSpeed:
                self.speed = newSpeed
        else:
            raise Exception("Type Error, The new speed is not an int")
        

    def setUnit(self,newUnit):
        if isinstance(newUnit,str):
            if self.unit != newUnit:
                self.unit = newUnit
        else:
            raise Exception("Type Error, the new unit is not a string")
    def setStopAction(self,stopAction):
        if isinstance(stopAction,str):
            if self.stopAction != stopAction:
                self.stopAction = stopAction
        else:
            raise Exception("Type Error, the new stop action is not a string")
    
    def getId(self):
        return self.id
    
    def getSpeed(self):
        return self.speed    

    def getRotation(self):
        return self.rotation

    def getMessageDict(self,amount,steering):
        dict = {
            "id":self.getId(),
            "amount":amount,
            "rotation":self.getRotation(),
            "speed":self.getSpeed(),            
            "unit":self.getUnit(),
            "steering":steering
        }
        return dict   

    def sendMessage(self,newDict):
        isValid = False
        if isinstance(newDict,dict):
            if self.currentMessageDict != newDict:
                self.currentMessageDict = newDict
                isValid = True
        return isValid