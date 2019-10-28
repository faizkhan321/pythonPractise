#Areeba Kausar

# Exercise 6.1
grades = int(input('Enter numeral grade: '))
if (grades <= 10 and grades >= 0):
    if (grades >= 8.5):
        print('A')
    elif (grades >= 7.5 and grades < 8.5):
        print('B')
    elif (grades >= 6.5 and grades < 7):
        print('C')
    elif (grades >= 5.5 and grades < 6):
        print('D')
    else:
        print('F')
else: print('Error')

# Exercise 6.2
# all conditionals are executed

# Exercise 6.3
count = 0
string = str(input('Supply a string: '))
if 'a' in (string.lower()):
    count += 1
if 'e' in (string.lower()):
    count += 1
if 'i' in (string.lower()):
    count += 1
if 'o' in (string.lower()):
    count += 1
if 'u' in (string.lower()):
    count += 1
print('There are', count, 'different vowels in the string')

# Exercise 6.4
from pcinput import getFloat
from math import sqrt

a = getFloat( "A: " )
b = getFloat( "B: " )
c = getFloat( "C: " )

if a == 0:
    if b == 0:
        print( "There is not even an unknown in this equation!" )
    else:
        print( "There is one solution, namely", -c/b )
else:
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        print( "There are no solutions" )
    elif discriminant == 0:
        print( "There is one solution, namely", -b/(2*a) )
    else:
        print( "There are two solutions, namely",
                (-b+sqrt(discriminant))/(2*a), "and",
                (-b-sqrt(discriminant))/(2*a) )
##Taken from official solutions
