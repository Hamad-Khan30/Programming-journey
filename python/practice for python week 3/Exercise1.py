class Rectangle:
    def __init__(self,width,lenght):
        self.width = width
        self.lenght = lenght
    def area(self):
        Area = self.lenght*self.width
        return Area
    def primeter(self):
        Perimeter = 2*(self.lenght*self.width)
        return Perimeter
values = Rectangle(4,7)
print(values.area())
print(values.primeter())