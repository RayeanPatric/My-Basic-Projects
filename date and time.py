import time
a = time.strftime('%d.%m.%Y')
b = time.strftime('%H:%M:%S %p')
c = time.strftime('%A')
d = time.tzname
print('The date, time, week day name and timezone are below respectively:\n')
print(' ', a)
print(' ', b)
print(' ', c)
print(' ', d)

e = input('\nPress Enter/Return to exit:')
