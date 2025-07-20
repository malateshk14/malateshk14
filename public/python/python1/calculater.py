from random import choice

print('-------Shri Ganesh---------')

print('1-> addition')
print('2-> substraction')

while True:
    choice = int(input('Enter the choice'))
    print('----------------')
    if choice in ("1", "2"):
        
        if choice == "1":
            choice = int(input('Enter the choice'))
