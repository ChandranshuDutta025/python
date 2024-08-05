class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        average = (marks1+marks2+marks3)/3
        print(f"Average marks for {self.name} is {average}") 

s1 = Student("Krishna",97,98,99) 

class Student1 :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        for val in self.marks:
            sum = 0
            sum += val
        average = sum/len(self.marks)
        print("New student data uploading...\n" f"Average marks for {self.name} is {average}")
            

s2 = Student1("Krishna",[97,98,99,66])
s2.average()

