class Rectangle:
    def __init__(self,width,lenght):
        self.width = width
        self.lenght = lenght
    def area(self):
        Area = self.lenght*self.width
        return Area
    def __str__(self):
        return (f"Rectangle {self.area()}")
values=Rectangle(4,5)
print("Rectangle 5x4 area" ,values.area())