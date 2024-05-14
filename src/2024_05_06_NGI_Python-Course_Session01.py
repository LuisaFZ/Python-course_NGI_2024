#   -*- coding: utf-8 -*-
"""
Spyder Editor

Created on Mon May  6 13:50:14 2024

@author: Luival 2024-05-06

"""
###################################
#    NGI Python course            #
#    Session 01 - May 6th 2024    #
###################################

#    Test functionality on spyder #

print('Hello world!')

#    datatypes: strings, integers, floats, print function

#    Exercise 1
print('Exercise 1: ')
print("Hello world!")
print('''Hello world!''')   # triple quote string
print('Hello world!')

#    strings
print('Hello worllllldd')  # single quote string
print("Hello wooooorld")  # double quote string

#    multi line string:
print('''
Hello
-
World
''')

#    integers: 1, 2, 3

#   floats: 1.2, 3.14, 100.99

#   int function converts a float into an integer BUT!!
#   it does not round it, only removes the numbers after the decimal
print(int(100.99))


#   operators +, - , * , / , **, // , %
print('Operators:')

print(1+3)
print(1-3)
print(4*3)
print(3**2)  # power, 3 to the power of 2 = (3*3)

print(10/3)
print(10//3)   # divide and floor, divides and rounds down to the nearest
#   integer, if one of the values is a float, you'll get back a float.

print(1 % 3)  # modulo, returns the remainder of the division


#   exercise 2
print('exercise 2')
print(5**8)    # power, 5 to the power of 8
print(9**0.5)  # workaround for squareroot of 9
print(14 % 5)  # modulo
print(13//33)  # prints the remainder


#  variables, and string concatenation
limestone_ucs = 130  # [Mpa]

#   string concatenation
print('the UCS of the sample is ' + str(limestone_ucs) + ' MPa')


# string formatting option 2
print('the UCS of the sample is {} MPa'.format(limestone_ucs))
print('the UCS of the sample is {} {}'.format(limestone_ucs, 'MPa'))

# string formatting option 3 using f strings
print(f'the UCS of the sample is {limestone_ucs} MPa')

# r strings: filepaths have \ , but \n and \t are pythons way to
# add new lines or tabs, this can encounter problems when
# your folder starts with n or t

filepath = r'C:/Users/luival/'

# \n adds a new line
# \t adds a tab


#   datatypes: lists [], tuples (), and dictionaries {},
#   index, exeptions / errors

soil_types = ['gravel', 'sandy_gravel', 'silt']
#   indexes= [   0    ,       1       ,   2    ] from the beginning
#   indexes= [  -3    ,      -2       ,  -1    ] from the end

print(soil_types)
print(soil_types[-3])
print(soil_types[-1])
print(soil_types[0])

#   adding elements to the list, by default at the end:

soil_types.append('clay')
print(soil_types)

#   add elements to a list in a specific place (index):

soil_types.insert(2, 'sand')
print(soil_types)

# tuples
soil_types_tuple = ('gravel', 'sandy_gravel', 'silt')

# dictionaries
rock_UCS = {'granite': [220, 200, 205],
            'limestone': [140, 130, 120],
            'eclogite': [250, 300, 270]}


#   EXERCISE 3
print('Exercise 3:')

#   create a list of srings
rock_types = ['marl', 'gneiss', 'limestone', 'eclogite']

#   create an empty list
empty_list = []

#   append items to empty_list, the items being integers from
#   counting characters from elements of the rock_types list

for rock in rock_types:
    len_char = len(rock)
    empty_list.append(len_char)

print(empty_list)

#   sum of three last items of the list [-3:]

sum_ex3 = 0

for item in empty_list[-3:]:
    print(item)
    sum_ex3 = sum_ex3 + item
print(f'the result is: {sum_ex3}')
