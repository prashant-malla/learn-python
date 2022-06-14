# Q1 - Practice: Define a function “gt5” that accepts 1 number argument; if that argument is greater than 5, return “yay!”.
def gt5(num):
    if num > 5:
        return "yay!"

# Q2 - Quiz: Define a function “reaction” that accepts 1 string argument; if that argument is “among us”, return “yay!”.
def reaction(x):
    if x == "among us":
        return 'yay!'

# Q3 - Practice: Define a function “gt5o” that accepts 1 number argument; if that argument is greater than 5, return “yay!”. Otherwise, return “nu!”
def gt5o(x):
    if x > 5:
        return "yay!"
    else:
        return "nu!"

# Q4 - Quiz: Define a function “reaction” that accepts 1 string argument; if that argument is “among us”, return “yay!”. Otherwise, return “nu!”
def reaction(x):
    if x == "amoung us":
        return "yay!"
    else: 
        return "nu!"

# Q5 - Practice: Define a function “blackjack” that accepts a list of numbers. If the sum of the numbers is less than 21, return the sum. Otherwise, return 0.
# def blackjack(list):
#     total = sum(list)
#     if total < 21:
#         return total
#     else:
#         return 0

# print(blackjack([1,2,31]))

# Q6 - Quiz: Define a function “can_cook” that accepts a list of strings. If the list of strings contains “lemon”, return the list. Otherwise, return an empty list. (Hint: “hello” in lst will return True if the variable “lst” contains the string “hello”)
# def can_cook(list):
#     if "lemon" in list:
#         return list
#     else:
#         return []

# print(can_cook(["lemon",'cauli']))

# Q7 - Quiz: Define a function “laugh” that accepts a list of booleans. If any of the booleans are True, return “haha”. Otherwise, return “uh”. (Hint: the any function will return True if any boolean in the input list is True)
# def laugh(list):
#     if any(list):
#         return "haha"
#     else:
#         return "hu!"
# print(laugh([False, False]))

# Q8 - Practice: Write a while loop that prints every number from 5 to 10.
# i = 5
# while i <= 10:
#     print(i)
#     i = i + 1

# Q9 - Quiz: Write a while loop that prints every odd number from 5 to 15.
# i = 5 
# while i <= 15:
#     print(i)
#     i = i + 2
#     # if (i % 2) != 0:
#     #     print(i)
#     # i = i +1

# Q10 - Quiz: Write a function “print_from_to” that accepts two number arguments and prints every number from the first argument to the second. For example, “print_from_to(3, 6)” would print all numbers from 3 to 6.
# def print_from_to(num1, num2):
#     while num1 <= num2:
#         print(num1)
#         num1  = num1 + 1

# print(print_from_to(2, 6))

# Q11 - Practice: Write a while loop that prints every number from 5 to 10 that is not a multiple of 3 (Hint: Use if statement)
# i = 5
# while i <= 10:
#     if (i % 3) != 0:
#         print(i)
#     i += 1

# Q12 - Quiz: Write a while loop that prints every number from 5 to 15 that is not a multiple of 6. (Hint: Use if statement)
i = 5
while i <= 16:
    if (i % 6) != 0:
        print(i)
    i += 1