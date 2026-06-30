class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "...."
class cat(animal):
    def speak(self):
        return "Meow"
class dog(animal):
    def speak(self):
        return "woof"
animals= [cat("Baerinjal"), dog("Sama")]
for animal in animals:
    print(f"{animal.name} says : {animal.speak()}")