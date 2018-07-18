from sales import Sari
from ude import MyException

if __name__ == '__main__':
    makhmali = Sari(1000, 2000)
    try:
        sP = makhmali.getSP(500)
        print('The selling price is', sP)
    except MyException as me:
        me.displayMsg()