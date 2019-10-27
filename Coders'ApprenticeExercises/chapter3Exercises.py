# Areeba Kausar

#Write a program that displays the number of seconds in a week
print(60*60*24*7)

#Exercise 3.1:
# Calculate the total wholesale costs for 60 copies.
books = 60
cover_price = (24.95 * books) * 0.60
shipping = 3 + (0.75*(books-1))
total_wholesale_cost = print(cover_price + shipping)

#Exercise 3.2:
# explain  the  errors:

#print( "A message" ). FULL STOP
# print( "A message') Common strings
# print('A messagef"') unmatched string

#Exercise 3.3:
#make Python raise a ZeroDivisionError
#print(9/0)

#Exercise 3.4:
#locate the problem:
print((2*3)/4 + (5-6/7)*8) #extra parenthesis but error was shown in line below
print(((12*13)/14 + (15-16)/17)*18)

#Exercise 3.5:
# Write program that prints the answer.
alarm = 14 + 535
print(alarm % 24)
