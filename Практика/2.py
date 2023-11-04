email = input()
if '@' in email and '.' in email:
    print('Валидный адрес электронной почты')
elif '@' not in email and '.' not in email:
    print('Отсутствует @ и .')
elif '.' not in email:
    print('Отсутствует .')
else:
    print('Отсутствует @')
