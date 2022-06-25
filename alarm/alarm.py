from random import choice

digits = list()
lowercase_letters = list()
uppercase_letters = list()
punctuation = list()

chars = list()

digits.extend('0123456789')
lowercase_letters.extend('qwertyuiopasdfghjklzxcvbnm')
uppercase_letters.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
punctuation.extend('!@#$%^&*,.?')

chars += lowercase_letters
chars += uppercase_letters

while True:
    pwd_length=int(input('Введите желаемую длину пароля: '))
    if 0 < pwd_length:
        break
    else:
        continue

while True:
    pwd_digits=input('Включить в пароль цифры (y, n): ')
    if pwd_digits == 'y':
        chars += digits
        break
    elif pwd_digits == 'n':
        break
    else:
        continue

while True:
    pwd_punctuation=input('Включить в пароль знаки пунктуации (y, n): ')
    if pwd_punctuation == 'y':
        chars += punctuation
        break
    elif pwd_punctuation == 'n':
        break
    else:
        continue

password = ''

for i in range(pwd_length):
   password += choice(chars)

print('\n', password, '\n', sep='')
