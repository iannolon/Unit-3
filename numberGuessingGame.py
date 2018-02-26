#IanNolon
#1/26/18
#numberGuessingGame.py

from random import randint

rnum = randint(1,100)
guess = 0
while guess != rnum:
    guess = int(input('Guess a number from 1 to 100: '))
    if guess > rnum:
        print('Too high')
    elif guess < rnum:
        print('Too low')
    else:
        print('Correct number')
        break
