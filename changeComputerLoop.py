#IanNolon
#2/28/18
#changeComputerLoop.py

change = int(input('Enter the number of cents you want in change: '))
quarters = 0
dimes = 0
nickels = 0
pennies = 0

while quarters * 25 <= change - 25:
    quarters = quarters + 1
change = change - quarters * 25
while dimes * 10 <= change - 10:
    dimes = dimes + 1
change = change - dimes * 10
while nickels * 5 <= change - 5:
    nickels = nickels + 1
change = change - nickels * 5
while pennies <= change - 1:
    pennies = pennies + 1

print('Quarters = ', quarters)
print('Dimes = ', dimes)
print('Nickels = ', nickels)
print('Pennies = ', pennies)
