import random

# x = random.randint(0,2)
# y = int(input('Guess what!!: '))
# while y != x:
#     print(x)
#     if x > y :
#         print('Bigger') 
#     elif x < y :
#         print('Smaller')
#     else:
#         print("good job👍!!")
#         break
#     print("Try again!! ")
    
#     y = int(input('Guess what!!: '))

# print('You finished😍')


# The code above is the inverse of the code below. In the code above, the system considers a number.


x = random.randint(0,99)

while True:
    print(x)
    y = input('it\'s true?!: ')
    # good job👍
    if y == 'd':
        break
    # Smaller
    elif y == 'k':
        x = random.randint(0,x)
    # Bigger
    elif y == 'b':
        x = random.randint(x,99)
    else :
        print("Error 404")

print('You finished😍')
