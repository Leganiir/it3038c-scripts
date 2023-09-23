#Random Number Game 1-10
import random

number = random.randint(1, 10)

print('Please guess a number between 1-10.')
while True:
    Guess = int(input())
    if Guess > 10 or Guess < 1:
        print('Number must be between 1-10')
    elif Guess > number:
        print('Guess was too high!')
    elif Guess < number:
        print('Guess was too low!')
    elif Guess == number:
        print('Yes, the number was ' + str(int(number)) + ', you win!')
        break
    

