#IanNolon
#2/28/18
#betterAdditionGame.py

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(0,10)
    num2 = randint(-5,5)
    sum = int(input('What is ' + str(num1) + '+' + str(num2) + '? '))
    break
