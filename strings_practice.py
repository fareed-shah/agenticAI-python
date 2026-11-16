# Problem 1

import math

# Square root of 256
print(math.sqrt(256))

# Value of Pi
print(math.pi)


# Problem 2

import random
random_number=random.randint(1,100)
print(random_number)


# Problem 3

# This programme prints Hello on the Screen

"""
This is a multi-liine commit
"""

print('Hello')

# Problem 4

import pyjokes # pyright: ignore[reportMissingImports]

pip_joke = pyjokes.get_joke()
print(pip_joke)


# Problem 5

import os

print(f" lists all the files and folders present in the current directory. \n {os.listdir()}")


# Problem 6

i=5
f=5.5
s='Fareed Shah'
b=True
x=None

print(f"data type of  variable i  : {type(i)}")
print(f"data type of  variable f  : {type(f)}")
print(f"data type of  variable s  : {type(s)}")
print(f"data type of  variable b  : {type(b)}")
print(f"data type of  variable x  : {type(x)}")


# Problem 7 

number_1 = int(input('Enter first number : '))
number_2 = int(input('Enter Second number : '))
add = number_1 + number_2

print(f"total : {add}")


# Problem 8 

num = input('Enter  number : ')
print(f" before type conversion  {type(num)}")
num=int(num)
print(f" after type conversion  {type(num)}")

# Problem 9

name='Fareed Shah'
age=28
is_Student = True

print(f"my name is : {name} my age is {age} student {is_Student} ")

# Problem 10

length = int(input("Enter length "))
breadth = int(input("Enter breadth "))
area= length * breadth

print(f" area of rectangle :  {area}")

# Problem 11

word = input("Enter any word to check it's length ")
print(f" word length is : {len(word)}")

# Problem 12

str = input("Enter any string ")
print(f" input string  in UPPER-CASE : {str.upper()}")
print(f" input string  in lowercase: {str.lower()}")

# Problem 13

sentence = input("Enter any  sentence ")
print(f" space replaced by an underscore (_) : {sentence.replace(' ','_')}")

# Problem 14

w = input('search any wprd..... ')

if  w.lower() == "python":
    print('Found')
elif w.upper() == "PYTHON":    
    print('Found')
elif w.capitalize() == "Python":    
    print('Found')    
else:
    print('Python,python OR PYTHON not found') 

# Problem 15

character = input('input any word..... ')

print(f"first character : {character[0]}")
print(f"last character : {character[-1]}")
print(f"reversed character : {character[::-1]}")