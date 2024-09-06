class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return (3.17 * ( self.radius * self.radius))
    
    def perimeter(self):
        
        return (self.radius * 3.17 * 2)
    
rad = int(input("Enter the radius of circle: "))
c1 = Circle(rad)
perimeter = c1.perimeter()
print(perimeter)
area = c1.Area()
print(area)
