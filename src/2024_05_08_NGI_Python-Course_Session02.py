# # -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:57:24 2024

@author: luival

"""

###################################
#    NGI Python course            #
#    Session 02 - May 8th 2024    #
###################################

#   Repetition session 01
#   variables

a_string = 'this is a string'
print(a_string)

an_integer = 5

a_float = 3.14

a_sum = 7 + 4.56
print(a_sum)

UCS_sample_01 = 30  # MPa
print(f'the rock UCS value is {UCS_sample_01} MPa')

filepath = (r'C:\Users\luival\.spyder-py3')

#   repetition: lists[] - tuples() - and dictionaries {}

a_list_of_numbers = [3, 4, 101, 15.3]

a_tuple = (4, 3, 2, 1)  # to modify a tuple turn it into a list, edit and
# revert back from list to tuple

a_dictionary_UCS = {'shale': 25, 'gneiss': 210}
# does not need/have indexing but has key/value pairs

#   Exercise 4

print('Exercise 4:')
# create a list and a tuple:
rock_list = ['gneiss', 'marl', 'limestone']
rock_tuple = ('gneiss', 'marl', 'limestone')

# print the first two items of both sequences

print(rock_list[:2])
print(rock_tuple[:2])

# append 'greenschist' to them

rock_list.append('greenschist')
#   rock_tuple.append('greenschist')  # gives an error, tuples are immutable

# exchange the second element of both sequences with 'dolomite'

rock_list.insert(1, 'dolomite')
#   rock_tuple.insert('dolomite')   # gives an error, tuples are immutable

print(rock_list)
print(rock_tuple)

#   control structures: conditional statements: if, elif, else, match cases.
#   operators

#   outputs are true or false

rock_1 = 'gneiss'
rock_2 = 'granite'

print(rock_1 == rock_2)  # == is equal to

print(rock_1 != rock_2)  # != is not equal to

rock_1_UCS = 190
rock_2_UCS = 200

#   greater than > , smaller than <
#   greater or equal to >= , less or equal to <=


print(rock_1_UCS < rock_2_UCS)
print(rock_1_UCS >= rock_2_UCS)


#   control structures: if elif else

if rock_1 == rock_2:
    print('the rocks are the same')
else:
    print('the rocks are not the same')

#   else
if rock_1 == 'granite':
    print('the rock is a granite')
elif rock_1 == 'gneiss':
    print('the rock is a gneiss')
else:
    print('the rock is something else')

#   if your code is getting many if/elif
#   match cases???


#   control structures, loops, while loops, for loop
#   while loops can run forever, for loops are always finite

a_number = 1

while a_number < 10:
    print(f'a_number is {a_number} and is less or equal to 10')
    a_number = a_number + 1

print(f'after the loop completes, a_number is {a_number}')

#   Exercise 5
#   create a list of all Fibonacci numbers until 200 using a while loop
#   each number is the sum of the two preceding ones.

print('Exercise 5:')

#  Initialize with the first two Fibonacci numbers
fibonacci_under_200 = [0, 1]

while fibonacci_under_200[-1] + fibonacci_under_200[-2] < 200:
    next_fibonacci = fibonacci_under_200[-1] + fibonacci_under_200[-2]
    fibonacci_under_200.append(next_fibonacci)

print(fibonacci_under_200)

# iterate over a list with a while loop += and an index

soil_types = ['cobbles', 'pebbles', 'gravel', 'sand', 'clay']
friction_angles = [44, 40, 38, 35, 37]
cohesions = [0, 20, 0, 0, 5]

index = 0

while index < len(soil_types):
    soil_types[index] = 'silty-' + soil_types[index]
    index += 1
print(soil_types)


# iterate over a list with a for loop +=

for soil_type in soil_types:
    print(soil_type)

for i in range(len(soil_types)):
    print(f'{soil_types[i]}: friction angle of {friction_angles[i]} degrees')

for i, soil_type in enumerate(soil_types):
    print(f'{soil_type}: c={cohesions[i]}, phi={friction_angles[i]}')


#   list comprehensions are fast but can compromise readability/explainability

# Exercise 6
# sum all multiples of 3 and 5 under 1000

print('Exercise 6:')

startnumber = 0
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        startnumber = startnumber + i
print(startnumber)

# Exercise 7
print('Exercise 7:')

rocks = ['granite', 'sandstone', 'basalt', 'limestone', 'tuff', 'quartzite',
         'kaolin', 'phonolite', 'gneiss', 'sand', 'diabase', 'black coal',
         'slate', 'andesite', 'andesite', 'gypsum and anhydrite', 'greywacke',
         'suevite']

START_YEAR = 2007
years = list(range(START_YEAR, START_YEAR+len(rocks)))

#   Write a scalable loop that prints out all rocks of the year since 2007
#   in the form “The rock of the year {year} was {rock}”;

for (y, r) in zip(years, rocks):
    print(f'The rock of the year {y} was {r}')
