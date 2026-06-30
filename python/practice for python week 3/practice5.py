class Book:
    def __init__(self,Title, pages):
        self.Title= Title
        self.pages= pages
    def __str__(self):
        return (f"{self.Title} and {self.pages} pages")
    def __len__(self):
        return len(self.pages)
book= Book("This is the pthon book", 100)
print(book.Title)
print(book.pages)
print(book)



class Dog:
    species = "Canis familiaris"
    def __init__(self, name):
       self.name = name 
print(Dog("Rex").species) 
print(Dog("Bella").species)