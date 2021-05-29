import random

# import test_module

# test randon integter
# random_int = random.randint(1,100)
# print(random_int)

# test random random float
# random_float = random.random()
# print(random_float)

# this is a test to check created module
# print(test_module.test)


# -------------------------challenge 1: create random coin toss, heads and tails-------------------------

# random_int = random.randint(1,2)
# if random_int == 1:
#   print('tails')
# else:
#   print('heads')

# -------------------------challenge 2: who will pay the bill-------------------------

# names = ['BOB','ANGELA','BEN','BATMAN','SUPERMAN']

# names = input('enters everyone names with comma seperated: ')
# names = names.split(',')

# >>METHOD 1 USE OF RANDOM int and use of indices
# random_int = random.randint(0,len(names) - 1)
# pay_bill = names[random_int]

# Method 2 use of random choice
# pay_bill = random.choice(names)

# print(f'{pay_bill} is going to buy the meals for today!')


# -------------------------challenge 2: nested list-------------------------
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[0][1])


# -------------------------challenge 3: treasure hunt-------------------------

sure = 'n'
x = 0
y = 0

while sure == 'n':
    row1 = ['🥶️', '🥶️', '🥶️']
    row2 = ['🥶️', '🥶️', '🥶️']
    row3 = ['🥶️', '🥶️', '🥶️']

    print(f'{row1}\n{row2}\n{row3}')

    final_row = [row1, row2, row3]
    place_holder = input('enter place position you want to mark as robo: ')
    x = int(place_holder[0]) - 1
    y = int(place_holder[1]) - 1
    final_row[x][y] = '🤖'

    print(f'{row1}\n{row2}\n{row3}')

    sure = input('is this correct y/n: ')

if int(place_holder) == 23:
    row1 = ['🥶️', '🥶️', '🥶️']
    row2 = ['🥶️', '🥶️', '❤️️']
    row3 = ['🥶️', '🥶️', '🥶️']
    print(f'{row1}\n{row2}\n{row3}')
    print('congratilations you got the heart')

else:
    print('better luck next time')
