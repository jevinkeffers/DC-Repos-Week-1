# 5. Print a Triangle consisisting of '*'
rows = int(input("Enter the number of rows:"))
for x in range(0, rows):
    for y in range(0, rows - x - 1): 
        print(end = " ") #This will print spaces at the top with the * where there are no spaces, for as many times as ROWS - x - 1
    for y in range(0, x + 1): #Initially value is 0 and execute 1 *.
        print("*", end = " ") #Prints increasing *'s with x + 1 per row
    print()

# #SOLVED with help from https://www.youtube.com/watch?v=k_B-5Aad7EU