def greet(name):
    print("Hello!", name)
    print("Wellcomme to the AI world")
    print("I hope you will be confortable here")
    print("-----------------------------------")
greet("Ali")
greet("hamad")
greet("Waqas")
greet("Abdullah")
greet("Numan")

# User give you name
def greet(name):
    print("Hello!", name)
    print("Wellcomme to the AI world")
    print("I hope you will be confortable here")
users = []
for i in range(50):
    name=input("Please Enter your name: ")
    users.append(name)
for user in users:
    greet(user)


