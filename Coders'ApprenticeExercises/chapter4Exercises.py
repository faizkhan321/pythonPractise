# Areeba Kausar

# Exercise 4.1
var1 = 3
var2 = 4
var3 = 6
average = (var1 + var2 + var3) / 3
print(average)

# Exercise 4.2
radius = 1
circle = (radius ** 2) * 3.142
print('Surface area of a circle with radius', radius, 'is', circle)

#Exercise 4.3

amount = 340  # $3.4
max_dollar = amount//100
print(max_dollar)
remaining_for_quarters = amount - max_dollar*100
max_quarters = remaining_for_quarters//25
print(max_quarters)
remaining_for_dimes = remaining_for_quarters - max_quarters*25
max_dimes = remaining_for_dimes//10
print(max_dimes)
remaining_for_nickels = remaining_for_dimes - max_dimes*10
print(remaining_for_nickels)
max_nickels = remaining_for_nickels//5
print(max_nickels)
remaining_for_pennies = remaining_for_nickels - max_nickels*5
print(remaining_for_pennies)

#Exercise 4.4
a= 17
b= 23
print( "a =", a, "and b =", b)
a+=b
b = a - b
a -= b
print( "a =", a, "and b =", b)