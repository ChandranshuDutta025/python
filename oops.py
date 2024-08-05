class student:
    @staticmethod
    def college_name():
        print("ABC college")#It would print the name of the college and it is same for all the students
    name = "Anonymous" #It would not print the name of the student because it is a class variable and object > class variable
    #default constructors
    def __init__(self) :
        pass
    #parameterized constructors
    def __init__(self, fullname,marks) :
        self.name = fullname #It would print the name of the student
        self.marks = marks
        print("New student data uploading...")

s1 = student("Krishna",97)
print(s1.name,s1.marks,s1.college_name)
s2 = student("Ravi",98)
print(s2.name,s2.marks,s2.college_name)
