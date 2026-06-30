'''
from openai import OpenAI
print("This is the test how openai work or not")
'''

try:
    age =int(input("Please Enter your age: "))
    print(f"After 10 years your age will be = {age+10}")
except ValueError:
    print("You give input only in digits please try again with with digits ")
finally:
    print("Thanks for using this age count tool")


try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print(f"After division: {num1/num2}")
except ZeroDivisionError:
    print("You did not divide by zero")    
except ValueError:
    print("Input only in digits")
finally:
    print("Thanks for using this tool")