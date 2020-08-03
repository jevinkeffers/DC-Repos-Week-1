# 9. Print a square

#UNDERSTANDING NESTED LOOPS IS IMPORTANT

width = 5
height = 5
y = 0
while y < height:
    x = 0
    while x < width:
        print('*', end='')
        x = x + 1
    print()
    y = y + 1

#solved with Sean's help