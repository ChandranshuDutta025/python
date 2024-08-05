class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def showNumber(self):
        print(self.real,"i +",self.imaginary, "j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImaginary = self.imaginary +num2.imaginary
        return Complex(newReal,newImaginary)
    
    def __sub__(self,num2):
        newReal = self.real -num2.real
        newImaginary = self.imaginary -num2.imaginary
        return Complex(newReal,newImaginary)


num1 = Complex(2,3)  
num1.showNumber()

num2 = Complex(5,3)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()
