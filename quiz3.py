#IanNolon
#3/5/18
#quiz3.py

i=-15
while i<=-9:
    print(i)
    i=i+1
for j in range(50,17,-4):
    print(j)
total = 0
k=-100
while k<=1000:
    total = total + k
    k = k + 2
print(total)
while True:
    text = input('Enter text: ')
    if str('alpaca') in text:
        break
    elif str('Alpaca') in text:
        break
