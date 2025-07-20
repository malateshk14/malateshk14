print('Shri Ganesh')

class InsufficientBalanceError(Exception):
    def __init__(self, accno, cb):
        self.__accno = accno
        self.__curbal = cb

class Customer:
    def __init__(self):
        self.__dct = {}
    def append(self, accno, n , bal):
        self.__dct[accno] = {'Name': n, 'Balance': bal}
    def deposit(self, accno, amt):
          d = self.__dct[accno]

