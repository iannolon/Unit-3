#IanNolon
#2/15/18
#unitConvertor2.py

while True:
    print('Choose an option!')
    print('1) Kilometers to Miles')
    print('2) Kilograms to Pounds')
    print('3) Liters to Gallons')
    print('4) Celsius to Fahrenheit')
    print('5) Quit the program')
    choice = int(input('Which one?'))
    if (choice == 1):
        km = float(input('Enter Kilometers'))
        print (km * 0.621371,' Miles')
    elif (choice == 2):
        kg = float(input('Enter Kilograms'))
        print (kg * 2.20462,' Pounds')
    elif (choice == 3):
        liters = float(input('Enter Liters'))
        print (liters * 0.264172,' Gallons')
    elif (choice == 4):
        cel = float(input('Enter Degrees in Celsius'))
        print (cel * 1.8 + 32,' Degrees Fahrenheit')
    elif (choice == 5):
        break
    else:
        print ('Error')
print('Have a nice day! Thanks for using out unit converter')
