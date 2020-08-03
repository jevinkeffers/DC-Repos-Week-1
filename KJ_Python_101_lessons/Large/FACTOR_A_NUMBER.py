# 2. Factor a Number
Given a number, print its factors.
def factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = 120 #Change number to create different solutions
factors(num)

# #SOLVED 