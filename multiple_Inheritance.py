# Description: Multiple Inheritance is a feature of object-oriented programming that allows a class
#  to inherit attributes and methods from more than one parent class.
class A:
    varA = "Welcome to the class A"
class B:
    varB ="Welcome to the class B"
class C(A,B):
    varC = "Welcome to the class C"

obj = C()
print(obj.varA)