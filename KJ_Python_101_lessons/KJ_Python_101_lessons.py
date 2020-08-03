    # https://dc-learning-portal.netlify.app/lessons/solving-problems-using-code/intro-to-python/#small
    #SMALL
    ##1. Hello You!
    #Prompt the user for his name using the input function. 
    # name = input('What is your name?' )
    # print('Hello,' + name + '!') 
    #solved

    #2. HELLO YOU!
    #Same as the first exercise, but this time print the user's name in ALL CAPS, and also tell them the number of letters in their name.
    #(Hint: You'll want to search for documentation on how to uppercase a string.)
    # name = input('WHAT IS YOUR NAME? ')
    # print('HELLO, ' + str(name.upper()) + '!')
    # print('YOUR NAME HAS ' + str(len(name)) + ' LETTERS IN IT! AWESOME!')
    #solved

    #3. MADLIB
    # name = input('Pick a name: ')
    # subject = input('Pick a school subject: ')
    # print('%s here says that %s is his favorite subject in school. What a clown.' % (name, subject))
    #solved

    # 4. Day of the Week
    # day = int(input('Day (0-6)? '))
    # if day == 0:
    #     print('Sunday')
    # if day == 1:
    #     print('Monday')
    # if day == 2:
    #     print('Tuesday')
    # if day == 3:
    #     print('Wednesday')
    # if day == 4:
    #     print('Thursday')
    # if day == 5:
    #     print('Friday')
    # if day == 6:
    #     print('Saturday')
    #solved

    # 5. WORK OR SLEEP IN?
    # day = int(input('Day (0-6)? '))
    # if day == 0 or day == 6:
    #     print('Sleep in')
    # elif day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
    #     print('Go to work')
    # else:
    #     print('Pick a number between 0-6')
    # #solved

    #6. C to F
    # Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user. 
    # temp = input("What's the temperature in Celsius? ")
    # fahrenheit = (int(temp) * 9/5) + 32
    # print("That is %s degrees in Fahrenheit." % fahrenheit)
    #solved

    # 7. Looping from 1 to 10
    #Using a while loop, print out the numbers between 1 and 10 inclusive, one on a line.
    # count = 0
    # while count < 10:
    #     count += 1
    #     print(count)
    # #solved

    # 8. n to m
    # Same as the previous problem, except you will prompt the user for the number to start on and the number to end on.
    # count = int(input("Start with: "))
    # end_count = int(input("End with: "))
    # while count <= end_count:
    #     print(count)
    #     count +=1 
    # #solved

    # 9. Print a square

    #UNDERSTANDING NESTED LOOPS IS IMPORTANT

    # width = 5
    # height = 5
    # y = 0
    # while y < height:
    #     x = 0
    #     while x < width:
    #         print('*', end='')
    #         x = x + 1
    #     print()
    #     y = y + 1

    #solved with Sean's help

    # 10. Print a Square II
    # Print a NxN square of * characters. Prompt the user for N. 
    # size = input("How big is the square? ")
    # width = int(size)
    # height = int(size)
    # y = 0
    # while y < height:
    #     x=0
    #     while x < width:
    #         print('*', end = '')
    #         x += 1
    #     print()
    #     y += 1    
    # #solved with Sean's help

    # #BUGFIX
    # count = 0
    # MAX = 10
    # while count < 10:
    #     count += 1
    #     if count % 2 == 0:
    #         print(count)

# #solved

#MEDIUM
#1. TIP CALCULATOR 
# Good -> 20%
# Fair -> 15%
# Bad -> 10%

# bill = float(input("Total bill amount? "))
# service = input("Level of service? ")
# lower_service = service.lower()
# tip = 0
# if lower_service == 'good':
#     tip = bill * .20
# elif lower_service == 'fair':
#     tip = bill * .15
# elif lower_service == 'bad':
#     tip = bill * .10
# else:
#     print('Invalid input')
# total = tip + bill
# print("Tip amount: $%.2f" % (tip))
# print("Total amount: $%.2f" % (bill + tip))
#SOLVED

# 2. Tip Calculator 2
# Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst. Example session:

# bill = float(input("Total bill amount?"))
# service = input("Level of service? ")
# split = int(input("Split how many ways? "))
# lower_service = service.lower()
# tip = 0
# if lower_service == 'good':
#     tip = bill * .20
# elif lower_service == 'fair':
#     tip = bill * .15
# elif lower_service == 'bad':
#     tip = bill * .10
# else:
#     print('Invalid input')
# total_per_person = (tip + bill) / split
# print("Tip amount: $%.2f" % (tip))
# print("Total amount: $%.2f" % (bill + tip))
# print("Amount per person: $%.2f" % total_per_person)
#SOLVED

# 3. How many coins?
# Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program.

# coins = 0
# answer = "yes"
# while answer == "yes":
#     print("You have %s coins." % coins)
#     answer = input("Do you want another? ")
#     if answer == "yes":
#         coins +=1
#     if answer == "no":
#         print("Bye")
# #SOLVED

# 4. Print a Box
# Given a height and width, input by the user, print a box consisting of * characters as its border.

# rows = int(input('How tall is the box? '))
# columns = int(input('How wide is the box? '))

# for x in range(0, rows):
#     for y in range(0, columns):
#         if(x == 0 or x == rows -1 or y == 0 or y == columns -1):
#             print('*', end = ' ')
#         else:
#             print(' ', end = ' ')
#     print()

# #SOLVED with help from https://www.codespeedy.com/python-program-to-print-hollow-box-pattern/

# 5. Print a Triangle consisisting of '*'
# rows = int(input("Enter the number of rows:"))
# for x in range(0, rows):
#     for y in range(0, rows - x - 1): 
#         print(end = " ") #This will print spaces at the top with the * where there are no spaces, for as many times as ROWS - x - 1
#     for y in range(0, x + 1): #Initially value is 0 and execute 1 *.
#         print("*", end = " ") #Prints increasing *'s with x + 1 per row
#     print()

# #SOLVED with help from https://www.youtube.com/watch?v=k_B-5Aad7EU

# # 6. Multiplication Table
# # Print the multiplication table for numbers from 1 up to 10.
# nums = range(1, 11)
# mult = range(1, 11)
# for i in nums:
#     for j in mult:
#         print(str(i) + ' x ' + str(j) + ' = ' + str(i * j))
# #SOLVED


# LARGE
# #1. Triangle Numbers
# Print the first 100 triangle numbers. What is a triangle number? Read this article to find out what triangle numbers are. https://www.mathsisfun.com/algebra/triangular-numbers.html

# count = 1
# triangle = 1

# while count <= 100:
#     print(triangle)
#     count += 1
#     triangle += count

#Elegant solution from Chris Owens here that I just couldn't work out but totally understand after seeing it

# 2. Factor a Number
#Given a number, print its factors.
# def factors(x):
#     for i in range(1, x + 1):
#         if x % i == 0:
#             print(i)

# num = 120 #Change number to create different solutions
# factors(num)

# #SOLVED 

# 3. Guess a Number
# You will implement a guess-the-number game where the player has to try guessing a secret number until they gets it right. For now, you will "hard code" the secret number to 5 (just set it to five like secret_number = 5). You will prompt the player to enter a number again and again, each time comparing their input to the secret number. To to that, you will need to write a while loop. If they guess correctly, you will print "You win!", otherwise, you will prompt for a number again.

#STEP 1

# n = 5
# print("I am thinking of a number between 1 and 10.")
# i = int(input("What's the number? "))
# if i == n:
#     print("Yes! You win!")
# while i != n:
#     int(input("Nope, try again. "))
#     print("Yes! You win!")
#     break
#SOLVED 

#STEP 2: Give High-Low Hint
#Improve your game to provide the player with a high-or-low hint.
# n = 5
# print("I am thinking of a number between 1 and 10.")
# guess = int(input("What's the number? "))
# if guess == n:
#     print("Yes! You win!")
# while guess != n:
#     if guess < n:
#         print("%d is too low" % guess)
#         guess = int(input("Guess again? "))
#     if guess > n:
#         print("%d is too high" % guess)
#         guess = int(input("Guess again? "))
#     if guess == n:
#         print("Yes! You win!")
#         break
#SOLVED

# Step 3: Randomly Generated Secret Number
# Instead of hard-coding the secret number to 5 now, you will generate the secret number using a random number generator provided by Python, so that even you, the programmer, cannot know the secret number before hand.

# import random
# my_random_number = random.randint(1, 10)

# print("I am thinking of a number between 1 and 10.")
# guess = int(input("What's the number? "))
# if guess == my_random_number:
#     print("Yes! You win!")
# while guess != my_random_number:
#     if guess < my_random_number:
#         print("%d is too low" % guess)
#         guess = int(input("Guess again? "))
#     if guess > my_random_number:
#         print("%d is too high" % guess)
#         guess = int(input("Guess again? "))
#     if guess == my_random_number:
#         print("Yes! You win!")
#         break
# #SOLVED

# Step 4: Limit Number of Guesses
# Limit the number of guesses the player has to 5. If he cannot guess the number within 5 guesses, he loses. Changing random number range to 1-20.

# import random
# my_random_number = random.randint(1, 20)

# print("I am thinking of a number between 1 and 20.")
# print("You have 5 guesses left.")
# guess = int(input("What's the number? "))
# number_of_guesses = 5
# guesses_made = 0
# while guess != my_random_number and (number_of_guesses -1) != guesses_made:
#     if guess < my_random_number:
#         print("%d is too low" % guess)
#         guesses_made += 1
#         guess = int(input("You have %d guesses remaining: Guess again? " % (number_of_guesses - guesses_made)))
#     elif guess > my_random_number:
#         print("%d is too high" % guess)
#         guesses_made += 1
#         guess = int(input("You have %d guesses remaining: Guess again? " % (number_of_guesses - guesses_made)))
# if(number_of_guesses - 1) == guesses_made:
#     print("Sorry, you ran out of guesses.")
# else:
#     print("Yes! You win!")

# #SOLVED

# Bonus: Play Again
# At the conclusion of a game, give the player the option of playing again.

import random
my_random_number = random.randint(1, 20)

def number_game(my_random_number):
    print("I am thinking of a number between 1 and 20.")
    print("You have 5 guesses left.")
    guess = int(input("What's the number? "))
    number_of_guesses = 5
    guesses_made = 0
    while guess != my_random_number and (number_of_guesses -1) != guesses_made:
        if guess < my_random_number:
            print("%d is too low" % guess)
            guesses_made += 1
            guess = int(input("You have %d guesses remaining: Guess again? " % (number_of_guesses - guesses_made)))
        elif guess > my_random_number:
            print("%d is too high" % guess)
            guesses_made += 1
            guess = int(input("You have %d guesses remaining: Guess again? " % (number_of_guesses - guesses_made)))
    if(number_of_guesses - 1) == guesses_made:
        print("Sorry, you ran out of guesses.")
        play_again = input("Would you like to play again? (Y or N) ").upper()
        if play_again == 'N':
            print("Bye.")
        if play_again == 'Y':
            import random
            number_game(my_random_number)
    else:
        print("Yes! You win!")
        play_again = input("Would you like to play again? (Y or N) ").upper()
        if play_again == 'N':
            print("Bye.")
        if play_again == 'Y':
            import random
            number_game(my_random_number)

number_game(my_random_number)

#CAN'T FIGURE OUT HOW TO CHANGE THE RANDOM NUMBER ON THE SUBSEQUENT PLAY-THROUGHS