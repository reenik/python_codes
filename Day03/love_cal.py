name1 = input('enter your name: ')
name2= input('enter second name: ')
love_string1 = 'true'
love_string2 = 'love'

full_name = (name1+name2).lower().replace(' ','')

score1 = 0
score2 = 0

for i in love_string1:
  score1 += full_name.count(i)

for i in love_string2:
  score2 += full_name.count(i)

score = (score1 * 10) + score2

print(f'for {name1} and {name2}, your total score is: {score}%')