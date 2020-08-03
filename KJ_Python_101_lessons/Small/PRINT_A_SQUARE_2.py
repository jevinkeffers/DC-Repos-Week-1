# 10. Print a Square II
# Print a NxN square of * characters. Prompt the user for N. 
size = input("How big is the square? ")
width = int(size)
height = int(size)
y = 0
while y < height:
    x=0
    while x < width:
        print('*', end = '')
        x += 1
    print()
    y += 1    
# #solved with Sean's help
