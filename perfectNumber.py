#IanNolon
#1/26/18
#perfectNumber.py

total = 0
num = int(input('Enter a number: '))
for i in range (1,num):
    if num % i == 0:
        total = total + i
if total == num:
    print('Perfect')
else:
    print('Not perfect')
