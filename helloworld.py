# print('Hello World')

greeting = 'Hello World Guys!'
def hello():
    name = input('enter your name')
    print(greeting + ', '+ name)

# hello()

# print(3 * '7')

def fab(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

# input  = int(input('enter a number'))
# print(fab(input))

def findOdd(arr):
    for i in arr:
        if arr.count(i) % 2 != 0:
            return i


# roll dice
def roll_dice(user_input):
    from random import randint
    random_value = randint(1, 6)
    if random_value == user_input:
        print('You win! the dice rolled a ' + str(random_value))
    else:
        print('You loose! The dice rolled a ' + str(random_value))

# num_a = int(input('enter a number between 1 and 6: '))
# roll_dice(num_a)

# convert celsius to farenheit
def c_to_f(c):
    f = c * 9/5 + 32
    return f

# print(c_to_f(10))

def funct(x):
    res = 0
    for i in range(x):
        res += i
    return res

# print(funct(4))

# def longest_word(words):
#     longest = ''
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest


# Some of the standard library's useful modules include string, re, datetime, math, random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.

# Different exceptions are raised for different reasons.
# Common exceptions:
# ImportError: an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly;
# TypeError: a function is called on a value of an inappropriate type;
# ValueError: a function is called on a value of the correct type, but with an inappropriate value.
