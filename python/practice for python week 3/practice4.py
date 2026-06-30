class circle:
    def __init__(self,r):
            self.r = r
    def area(self):
          self.area = 3.14 * self.r**2
          return self.area
class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
         self.side= self.side**2
         return self.side
shapes = [circle(5),Square(7),circle(7),Square(2)]
for shape in shapes:
     print(shape.area())