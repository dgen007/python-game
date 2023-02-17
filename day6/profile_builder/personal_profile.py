from person import fullname as name
from bmi_calculator import bmi



person_name = name()
person_bmi = bmi(95,190)

print(f"This person's name is {person_name},with value {person_bmi}")
print("This person's name is", person_name,"with value",person_bmi)


#Create a calculator
#Create addition.py, add a function to add two numbers
#Create subtract.py, add a function to subtract two numbers
#Create divide.py, add a function to divide two numbers
#Create multiply.py, add a function to multiply two numbers
#Import all files into calculator.py
#Call the functions from each module or python file
def add(x,y):
    return x + y
