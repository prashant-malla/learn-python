# how print works?
print('patt', end="")
print('er', end="")
print('ns!')

def pattern1(n): # rectangle square
    for row in range(n):
        for col in range(n):
            print('*', end="")
        print()
# pattern1(5)

def pattern2(n): # left triangle
    for row in range(n):
        for col in range(row):
            print('*', end="")
        print()
# pattern2(5)

def pattern3(n):# right triangle
    for row in range(n):
        for spc in range(n-row):
            print(" ", end="")
        for col in range(row):
            print('*', end="")
        print()
# pattern3(5)

def pattern4(n): #left downward triangle
    for row in range(n):
        for col in range(n-row):
            print("*", end="")
        print()
# pattern4(5)

def pattern5(n): #right downward triangle
    for row in range(n):
        for spc in range(row):
            print(" ", end="")
        for col in range(n - row):
            print("*", end="")
        print()
# pattern5(5)

def pattern6(n): # pyramid pattern
    for row in range(n):
        for spc in range(n - row - 1):
            print(' ', end="")
        for col in range(2 * row + 1):
            print('*', end="")
        print()
pattern6(5)