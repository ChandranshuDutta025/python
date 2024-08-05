class Car:
    @staticmethod
    def start():
        print("Car is starting")
    @staticmethod
    def stop():
        print("Car stopped..")
class Audi(Car):#single inheritance
    def __init__(self,Brand):
        self.Brand = Brand

class Q4(Audi):#multilevel inheritance
    def __init__(self,Model):
        self.Model = Model

car1 = Q4("Diesel")

car1.start()
