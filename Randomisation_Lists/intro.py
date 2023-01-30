#its basically used to generate random numbers

import random as rd

#generate random integer numbers using range 0-10
random_integer =  rd.randint(0,10)
print(random_integer)

#generates a floating random from 0.0000-0.9999, 
# to generate the decimal number we can use multiplication
 

randoam_float = rd.random() * 5
print(randoam_float)


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)  # Find next banana starting at position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()

#print the list of Squred items

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)


#nested List

a = [1,2,3]
b = [4,5,6]
c=[a,b]

print(c)

#nested loop another one

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][2])  #prints 2nd list 3rd item
print(dirty_dozen[1][3])