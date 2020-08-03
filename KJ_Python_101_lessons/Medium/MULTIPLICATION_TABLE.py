# 6. Multiplication Table
# Print the multiplication table for numbers from 1 up to 10.
nums = range(1, 11)
mult = range(1, 11)
for n in nums:
    for m in mult:
        print(str(n) + ' x ' + str(m) + ' = ' + str(n * m))
#SOLVED
