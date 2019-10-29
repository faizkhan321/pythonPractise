#Areeba Kausar
import random

counter = 10
while (counter != 1):
    print(counter)
    counter -= 1
print('Blast Off')

#Exercise 7.1
number = int(input('Enter a number: '))
counter = 1
while (counter < 11):
    print(str(counter), '*', str(number),'=', str(counter * number))
    counter += 1

#Exercise 7.2
number = int(input('Enter a number: '))
for counter in range(11):
    print(str(counter), '*', str(number),'=', str(counter * number))

#Exercise 7.3
lst = []
divisble_counter = 0
for i in range(10):
    number = int(input('Enter a number: '))
    lst.append(number)
print(max(lst))
print(min(lst))
for i in lst:
    if i // 3 == 0:
        divisble_counter += 1
print(divisble_counter)

#Exercise 7.4
for i in range(10,0,-1):
    print(str(i), 'bottles of beer on the wall,', str(i), 'bottles of beer')

#Exercise 7.5
lst = []
lst.append(1)
lst.append(1)
i = 0
n = 2
while (n < 900):
    n = lst[i] + lst[i+1]
    lst.append(n)
    i += 1
print(lst)

#Exercise 7.6
word_a = str(input('First word: '))
word_b = str(input('Second word: '))
character_string = ''
counter = 0

for characters in word_a:
    if characters in word_b:
        if characters in character_string:
            pass#print('repetition')
        else:
            counter += 1
            character_string += characters
            #print(characters)
    else:
        pass#print('character not match')

print('common character is', character_string, 'repeated', counter, 'times.')

#Exercise 7.8
number = random.randint(1,1001)
print(number)
guess = 0
counter = 1;
while (guess != number):
    guess = int(input('Guess number: '))
    if (guess > number):
        print('Lower')
    elif (guess < number):
        print('Higher')
    elif (guess == number):
        print('You guessed it in', counter, 'tries.' )
        break
    counter += 1

#Exercise 7.9
highest = 1001
lowest = 1
counter = 1
while True:
    guess = (highest + lowest)//2
    response = input ('Is number ' + str(guess) +' correct(C), higher(H) or lower(L) ')
    if response == 'C':
        print('I guessed it in', counter, 'tries.')
        break
    elif response == 'H':
        lowest = guess
    elif response == 'L':
        highest = guess
    if (highest - lowest == 0):
        print('cheater')
        break



