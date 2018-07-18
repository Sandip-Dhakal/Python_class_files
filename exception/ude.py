class MyException(Exception):

    def __init__(self, num):
        self.num = num
        msg = 'The value is less by '+ str(num)
        super(MyException, self).__init__(msg)

    def displayMsg(self):
        print('The amount is less by', self.num)