#Areeba Kausar
import math
import random

# Exercise 5.1
string = input("Enter a string: ")
print(len(string))

#Exercise 5.2
side1 = int(input('Enter first side: '))
side2 = int(input('Enter second side: '))
side3 = print(pow( (pow(side1,2) + pow(side2,2)),0.5))

#Exercise 5.3
num1 = int(input('Enter first num: '))
num2 = int(input('Enter second num: '))
num3 = int(input('Enter second num: '))

print(max(num1, num2, num3))
print(min(num1, num2, num3))
print(round(num1+num2+num3)/3,2)

#Exercise 5.4
print(round(math.exp(1)**-1, 5))
print(round(math.exp(1)**0, 5))
print(round(math.exp(1)**1, 5))
print(round(math.exp(1)**2, 5))
print(round(math.exp(1)**3, 5))

#Exercise 5.5
print(int(random.random()*10))
