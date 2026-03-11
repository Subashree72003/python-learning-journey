"""
from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def run(self):
        print("car is running")
class car(vehicle):
    def start(self):
        print("car started")

c = car()
c.start()
c=vehicle()
c.start()

"""
from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class credit_card(payment):
    def pay(self):
        print("credit card")

class UPI(payment):
    def pay(self):
        print(" DONE BY UPI")

C1 = credit_card()
C1.pay()
C2= UPI()
C2.pay()



