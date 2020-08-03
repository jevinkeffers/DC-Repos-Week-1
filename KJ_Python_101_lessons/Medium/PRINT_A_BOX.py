# 4. Print a Box
#Given a height and width, input by the user, print a box consisting of * characters as its border.

rows = int(input('How tall is the box? '))
columns = int(input('How wide is the box? '))

for x in range(0, rows):
    for y in range(0, columns):
        if(x == 0 or x == rows -1 or y == 0 or y == columns -1):
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()

# #SOLVED with help from https://www.codespeedy.com/python-program-to-print-hollow-box-pattern/