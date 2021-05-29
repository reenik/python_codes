yr = int(input('enter year: '))
message = ''

if yr % 100 == 0:
  if yr % 400 == 0:
    message = 'yr is leap yr.'
  else:
    message = 'yr is not leap yr.'

elif yr % 4 == 0:
  message = 'yr is a leap yr..'

else:
  message = 'yr is not a leap yr..'

print(f'{yr} {message}')