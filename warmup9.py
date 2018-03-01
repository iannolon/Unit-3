#IanNolon
#3/1/18
#warmup9.py

text = input('Enter text: ')
for ch in text:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print(ch.upper())
    else:
        print(ch)
