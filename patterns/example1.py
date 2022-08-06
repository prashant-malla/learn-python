# 1. Increasing Triangle Pattern
def pattern1():
    for row in range(5):
        for col in range(row + 1):
            print('* ', end="")
        print()
# pattern1()    

# 2. Decreasing Triangle Pattern
def pattern2():
    for row in range(5):
        for col in range(row, 5):
            print('* ', end="")
        print()
# pattern2()  

# 3. Increasing Right Sided Triangle
def patter3():
    n = 5
    for row in range(n):
        for spc in range(row, n):
            print(' ', end="")
        for col in range(row+1):
            print("*", end="")
        print()
# patter3()

# 4. Decreasing Right Sided Triangle
def pattern4():
    n = 5
    for row in range(n):
        for spc in range(row):
            print(' ', end="")
        for col in range(row, n):
            print('*', end="")
        print()
# pattern4()

# 5. Hill Side Pattern
def pattern5():
    n = 5
    for row in range(n):
        for spc in range(row, n):
            print(' ', end="")
        for col in range(row):
            print('*', end="")
        for col in range(row+1):
            print('*', end="")
        print()
# pattern5()

# 6. Reverse Hill Side Pattern
def pattern6():
    n = 5
    for row in range(n):
        for spc in range(row):
            print(" ", end="")
        for col in range(row, n-1):
            print("*", end="")
        for col in range(row, n):
            print("*", end="")
        print()
# pattern6()

# 7. Diamond Pattern
def pattern7():
    n = 5
    for row in range(n-1):
        for spc in range(n - row -1):
            print(' ', end='')
        for col in range(row):
            print('*', end='')
        for col in range(row +1 ):
            print('*', end="")
        print()
    for row in range(n):
        for spc in range(row):
            print(' ', end='')
        for col in range(row, n-1):
            print('*', end='')
        for col in range(row, n):
            print('*', end="")
        print()
pattern7()