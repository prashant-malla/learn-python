# Q1 - Practice: Define a function “print_list” that accepts a list of strings and, for all strings, prints the string.
def print_list(list):
    for i in list:
        print(i)

# Q2 - Quiz: Define a function “print_gt3” that accepts a list of numbers and, for all numbers, prints whether it is greater than 3 or not.
def print_gt3(list):
    for i in list:
        if i > 3:
            print('greter than 3')
        else:
            print("not greater than 3")

# Q3 - Quiz: Define a function “print_add3” that accepts a list of numbers and, for all numbers, prints 3 more than the number.
def print_add3(list):
    for i in list:
        print(i + 3)

# Q4 - Practice: Define a function “print_a_names” that accepts a list of names and, for all names, prints the name only if the name starts with an “A”. 
# Hint: The string method “startswith” accepts 1 string argument and checks if the string starts with that argument.
# def print_a_names(name_list):
#     for name in name_list:
#         if name.startswith("A"):
#             print(name)
# print_a_names(["Ram", "Amar"])

# Q5 - Quiz: Define a function “print_nums_gt3” that accepts a list of numbers and only prints numbers greater than 3.
# def print_nums_gt3(number_list):
#     for number in number_list:
#         if number > 3:
#             print(number)

# print_nums_gt3([1,2,3,4,5])

# Q6 - Practice: Define a function “get_name” that accepts a list of names and returns the first name that starts with “A”.
def get_name(names):
    for name in names:
        if name.startswith("A"):
            return name

# Q7 - Quiz: Define a function “get_odd” that accepts a list of numbers and returns the first number that is odd.
# Hint: You can check if a number is odd by using “x % 2 == 1”. The “%” is a modulo operator, so “x % 2” is 0 if x is even and 1 if x is odd.
def get_odd(numbers):
    for number in numbers:
        if number % 2 == 1:
            print(number)

get_odd([1,2,3,4,5,6])