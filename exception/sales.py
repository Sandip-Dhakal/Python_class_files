from ude import MyException

class Sari:

    def __init__(self, cP,mP):
        self.cP = cP
        self.mP = mP

    def getSP(self, discount):
        selling =  self.mP - discount
        if(selling < 1.5*self.cP):
            lessAmount = 1.5*self.cP - selling
            raise MyException(lessAmount)
        else:
            return selling


    