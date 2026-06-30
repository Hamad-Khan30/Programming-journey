name= str(input("What is your Name: "))
print(f" Your name is very beautiful {name}")
if len(name) < 6:
    print("But your name charters is too less")

age= int(input("What is your age: "))
Age= age + 10
print("After 10 years your age will be: ", Age)

a = 46
guess_number = int(input("please guess a number:"))
if guess_number == a:
    print("Oh! wow.....Your number is exactly right")
elif guess_number < 20 and guess_number > 0:
    print("Your guess is too low")
elif guess_number > 20 and guess_number < 43:
    print("Guess little bit higher number")
elif guess_number > 43 and guess_number <= 48:
    print("You are too close please try next time exactly")
elif guess_number < 60 and guess_number >= 48:
    print("Guess little bit higher number")
else: 
    print("Your number is too high")

