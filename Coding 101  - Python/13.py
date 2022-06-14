# iterable = range(10)
# print(list(iterable))

# loop
# for loop

# for i in range(10):
#     print(i)

# message = "nice to meet you"
# for i in message:
#     print(i)

def check(password):
    has_number = False
    for i in password:
        if i.isdigit():
            has_number = True
    return has_number

password = input('Password: ')
has_number = check(password)
print(has_number)