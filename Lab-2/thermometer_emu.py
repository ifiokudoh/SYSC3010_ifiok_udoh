#Thermometer emulator that generates random temperature continously
#Author Ifiok Udoh
#
import random
from threading import Thread
class thermometer(object):

    """
    Continously generates Random temperature value within limits start 
    and stop
    """
    def random_Temp(self, start, stop):
        while(self._generate == 1):
            # print(stop)
            self._temperature = random.randint(start,stop)

    def __init__(self):
        self._temperature = 0 
        self._generate = 1
        self._tempThread = Thread(target=self.random_Temp, args=(0,40))
        self._tempThread.start()
        

    def read(self):
        return self._temperature

    def close(self):
        self._generate = 0

# def main():
#     thermo = thermomether()
#     print("here")
#     print(thermo.read())
#     thermo.close()

# if __name__ == "__main__":
#     main()