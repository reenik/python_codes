print('Welcome to Bill-Split/Tip-Calculator')
total_bill = float(input('What is your tatal bill? '))

no_peoples = int(input('How many people to split the bill with? '))

while no_peoples <= 0:
  print('please enter proper amount of people')
  no_peoples = int(input('How many people to split the bill with? '))

tip_percent = int(input('''what percentage of tip you want to provide:
1. 5%
2. 10%
3. 15%
4. 20%
'''))

total_bill_per_person = (total_bill + (total_bill * (tip_percent/100))) / no_peoples

# print('Per person needs to pay in round number:',round(total_bill_per_person,2))

print(f'for total bill of {total_bill}, each one has to pay {round(total_bill_per_person,2)} inc. tip of {tip_percent}%')
# print(int(no_peoples) > 0)
