# 3. How many coins?
# Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program.

coins = 0
answer = "yes"
while answer == "yes":
    print("You have %s coins." % coins)
    answer = input("Do you want another? ")
    if answer == "yes":
        coins +=1
    if answer == "no":
        print("Bye")
# #SOLVED