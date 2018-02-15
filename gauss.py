#IanNolon
#1/15/18
#gauss.py

startNum = int(input('Enter a starting number '))
endNum = int(input('Enter an ending number '))
interval = int(input('Enter an interval between the addition '))
if startNum < endNum and interval >= 1:
    total = 0
    for i in range(startNum,endNum+1,interval):
        total +=i
    print('The sum of the numbers from ',startNum,' to ',endNum,' is ',total) 
else:
    print('Bad numbers')
