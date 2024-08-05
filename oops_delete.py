class Student:
    def __init__(self):
        print("Constructor called")
    def name(self):
        print("Constructor called")

s1 = Student()
print(s1.name())
del s1
print(s1.name())