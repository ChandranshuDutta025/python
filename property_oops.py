class student:
    def __init__(self,phy,chem,maths):
        self.chem = chem
        self.phy = phy
        self.maths = maths

    @property
    def percentage(self):
        return str((self.chem+self.maths+self.phy)/ 3) + "%"

s1 = student(99,97,98)
print(s1.percentage)

s1.phy = 88
print(s1.percentage)
