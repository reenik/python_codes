import random

# print(random.randint(1,3))

user_val = int(input('give your input based on following choices:\n\n1: 👊\n2: ✋\n3: 🖖\n'))
com_val = random.randint(1,3)

if (user_val == 1) and (com_val == 2):
  print('computer wins')
elif (user_val == 1) and (com_val == 3):
  print('user wins')
elif (user_val == 2) and (com_val == 3):
  print('computer wins')
elif (user_val == 2) and (com_val == 1):
  print('user wins')
elif (user_val == 3) and (com_val == 1):
  print('computer wins')
elif (user_val == 3) and (com_val == 2):
  print('user wins')
else:
  print('match draw')