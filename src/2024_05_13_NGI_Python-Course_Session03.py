# # -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:00:24 2024

@author: luival

"""

###################################
#    NGI Python course            #
#    Session 03 - May 13th 2024   #
###################################


# repetition last week - control structures: conditional statements and loops

weather = 'nice'

if weather == 'bad':
    print('dont cut your hair')
elif weather == 'nice':
    print('get a haircut')
else:
    print('check the weather forecast')

good_weather = True

if good_weather == True:
    print('wear sunscreen, but check your code style')
if good_weather is True:
    print('wear sunglasses')
if good_weather:
    print('wear sunscreen')

#   3 wasy to evaluate True/False: "=="  "is" and "if good_weather:" but
#   pycodestyle E712 does not like "==" and gives therefore a style warning


if good_weather:
    print('enjoy the good weather, but check your code style')
#   removing the '== True' also works, but it is less readable

counter = 0

while good_weather is True:
    print('we enjoy the sun')
    counter += 1
    if counter > 10:
        good_weather = False

####################################################

a_list = [1, 2, 3, 4, 5, 6, 7]
b_list = [71, 26, 53, 44, 35, 26, 17]
aplusb_list = []

for i in range(len(a_list)):
    aplusb = a_list[i] + b_list[i]
    aplusb_list.append(aplusb)

print(aplusb_list)

#   method vs function

aplusb_list.sort()    # sorting the list in ascending order
print(aplusb_list)


#   Exercise 3 (bonus)
print('Exercise 3 (bonus):')

rock_types = ['marl', 'gneiss', 'limestone', 'eclogite']

# create empty list
empty_list = []

#   append items to the previous list and replace the strings for the count
#   of characters on each original string
for rock in rock_types:
    len_char = len(rock)
    empty_list.append(len_char)

print(empty_list)

subset_list = empty_list[-3:]

result = sum(int(i) for i in subset_list)

print(f'The result is: {result}')

#   using the format method: PENDING!!
print("The result is: {}".format(result))

# Exercise 8
print('Exercise 8:')

rock_list = ['gneiss', 'marl', 'limestone']
ucs_list = [150, 45, 90]

# Create a dictionary by zipping rock_list and ucs_list
rock_ucs_dict = dict(zip(rock_list, ucs_list))

# adding a new key-value pair to the dictionary
rock_ucs_dict['sandstone'] = '50'
print(rock_ucs_dict)

for rock in rock_ucs_dict.keys():
    print(f'the {rock} has a UCS of {rock_ucs_dict[rock]} MPa')

#   Exercise 9
print('Exercise 9:')

number_list = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]

#   for the mean value:
mean_list = sum(number_list) / len(number_list)

print(f"the mean value is {mean_list:.2f}")  # 2f rounds to 2 decimals

# For the median, sort the list
number_list.sort()

# Determine the middle values
length = len(number_list)
middle_index = length // 2   # calculates the index of the middle element


# check if the list has even eller odd elements
if length % 2 == 0:
    # Even number of elements on the list
    median_value = (number_list[middle_index-1] + number_list[middle_index])/2
else:
    # Odd number of elements on the list
    median_value = number_list[middle_index]

print(f"the median value is {median_value:.2f}")

#   for the variance:
#   Calculate the squared differences
squared_diff = sum((x - mean_list) ** 2 for x in number_list)

# Estimate the variance
variance = squared_diff / len(number_list)

print(f"the variance is {variance:.2f}")

#   estimate the standard deviation
#   which is the square root of variance

sqroot_variance = variance ** 0.5

print(f"the standard deviation is {sqroot_variance:.2f}")


#   ### Functions ###


def hello_world():
    print('hello world!')   # basic printing function


hello_world()    # calling the function to produce output


def custom_substraction(a, b):
    return a - b    # function with inputs and outputs


def custom_substraction_int(a: int, b: int) -> int:
    '''this is a custom subtraction function'''
    return a - b
#   the same as above but specifying datatypes expected, in this case integers


print(custom_substraction(55, 16))  # calling the function to produce output


#   methods vs functions:
#   methods and functions work in the same way but methods
#   always belong to an object and functions are object independent

another_list = [3, 2, 1, 3, 2, 1]
# to sort a list with a method
another_list.sort()
print(another_list)
another_list.insert(3, 123)  # inserts '123' on index 3
print(another_list)
# sort a list with a function
another_list = sorted(another_list)
print(another_list)


#   Exercise 10, repeat exercise 9 but using functions instead
print('Exercise 10:')

number_list = [1, 2, 3, 1, 3, 3, 2, 1, 4, 6, 4, 1]


def mean(number_list):
    return sum(number_list) / len(number_list)  # function for the mean


#   function for the median
def median(number_list):
    number_list.sort
    length = len(number_list)
    middle_index = length // 2

    if length % 2 == 0:
        # Even number of elements on the list
        median_value = (number_list[middle_index-1] +
                        number_list[middle_index])/2
    else:
        # Odd number of elements on the list
        median_value = number_list[middle_index]
    return median_value


#   function for the variance
def variance(number_list):
    #   Calculate the squared differences
    squared_diff = sum((x - mean) ** 2 for x in number_list)

    # Estimate the variance
    variance = squared_diff / len(number_list)
    return variance


def std_dev(number_list):   # function for the standard deviation
    # Calculate the variance
    variance = sum((x - sum(number_list) / len(number_list)) **
                   2 for x in number_list) / len(number_list)
    # Calculate the standard deviation
    std_deviation = variance ** 0.5
    return std_deviation


#   genarating outputs using functions defined above:

# mean
mean = mean(number_list)
print(f'mean value = {round(mean, 2)}')

# median
median = median(number_list)
print(f'median value = {round(median, 2)}')

# var
var = variance(number_list)
print(f'variance = {round(var, 2)}')

# std
std = std_dev(number_list)
print(f'standard deviation = {round(std, 2)}')


# default values can be set for the input arguments of a function
def state_of_weather(state: str = 'good') -> None:
    print(f'today the weather is {state}')


state_of_weather('sunny')


# coding style, Zen of Python
# check the zen of python by writing: "import this" in the console
