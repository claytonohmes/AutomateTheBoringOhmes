#This is a guess the number game
#use the import function to bring in the random library
import random

#ask the user their name
print('Hello, what is your name?')
name = input()

print('Hi, ' + name + ', I am thinking of a number between 1 and 20.')
#Set secret number variable. use the randint function from the random library.
secretnumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretnumber:
        print('Your Guess is too low.')
    elif guess > secretnumber:
        print('Your guess is too high.')
    else:
        break # this is for guessing the correct number.

# if the correct number is guessed you will be broken out of the above for loop and end up here.
# if not, you will end up here at the end of the loop and trigger the else condiion.
if guess == secretnumber:
    print('Good job ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(secretnumber))
