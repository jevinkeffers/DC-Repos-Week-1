# LARGE
# #1. Triangle Numbers
# Print the first 100 triangle numbers. What is a triangle number? Read this article to find out what triangle numbers are. https://www.mathsisfun.com/algebra/triangular-numbers.html

count = 1
triangle = 1

while count <= 100:
    print(triangle) 
    count += 1
    triangle += count

#Elegant solution from Chris Owens here that I just couldn't work out but understand now after reading more about it