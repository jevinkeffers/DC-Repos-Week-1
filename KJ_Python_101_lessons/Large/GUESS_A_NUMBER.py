# # 3. Guess a Number
# # You will implement a guess-the-number game where the player has to try guessing a secret number until they gets it right. For now, you will "hard code" the secret number to 5 (just set it to five like secret_number = 5). You will prompt the player to enter a number again and again, each time comparing their input to the secret number. To to that, you will need to write a while loop. If they guess correctly, you will print "You win!", otherwise, you will prompt for a number again.

# #STEP 1

n = 5
print("I am thinking of a number between 1 and 10.")
i = int(input("What's the number? "))
if i == n:
    print("Yes! You win!")
while i != n:
    int(input("Nope, try again. "))
    print("Yes! You win!")
    break
# #SOLVED 

#STEP 2: Give High-Low Hint
#Improve your game to provide the player with a high-or-low hint.
n = 5
print("I am thinking of a number between 1 and 10.")
guess = int(input("What's the number? "))
if guess == n:
    print("Yes! You win!")
while guess != n:
    if guess < n:
        print("%d is too low" % guess)
        guess = int(input("Guess again? "))
    if guess > n:
        print("%d is too high" % guess)
        guess = int(input("Guess again? "))
    if guess == n:
        print("Yes! You win!")
        break
# #SOLVED

# # Step 3: Randomly Generated Secret Number
# # Instead of hard-coding the secret number to 5 now, you will generate the secret number using a random number generator provided by Python, so that even you, the programmer, cannot know the secret number before hand.

# import random
# my_random_number = random.randint(1, 10)

print("I am thinking of a number between 1 and 10.")
guess = int(input("What's the number? "))
if guess == my_random_number:
    print("Yes! You win!")
while guess != my_random_number:
    if guess < my_random_number:
        print("%d is too low" % guess)
        guess = int(input("Guess again? "))
    if guess > my_random_number:
        print("%d is too high" % guess)
        guess = int(input("Guess again? "))
    if guess == my_random_number:
        print("Yes! You win!")
        break
# # #SOLVED

# # Step 4: Limit Number of Guesses
# # Limit the number of guesses the player has to 5. If he cannot guess the number within 5 guesses, he loses. Changing random number range to 1-20.

import random
my_random_number = random.randint(1, 20)

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
else:
    print("Yes! You win!")

# # #SOLVED

# Bonus: Play Again
# At the conclusion of a game, give the player the option of playing again.

import random

def number_game():
    my_random_number = random.randint(1, 20)
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
            number_game(my_random_number)
    else:
        print("Yes! You win!")
        play_again = input("Would you like to play again? (Y or N) ").upper()
        if play_again == 'N':
            print("Bye.")
        if play_again == 'Y':
            number_game(my_random_number)

number_game(my_random_number)
