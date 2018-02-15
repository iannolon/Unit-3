#IanNolon
#1/15/18
#printStars.py

size = int(input('Enter a number for the number of rows you want your SYMMETRIC pyramid to have'))
if size<=23 and size >=1:
    row = 0
    while row <size+1:
        print(' '*(size-row+1),' *'*row)
        row += 1
elif size>23:
    print('Too big of a number, try again.')
elif size == 0:
    print('0')
else:
    print('imagine a negative pyramid')
