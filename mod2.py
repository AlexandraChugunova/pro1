password = input ('Введите пароль')
password_length = len(password)
check='Ваш пароль состоит только из цифр'

try:
    first_check = 1/password_length
    second_check = int(password)
except ZeroDivisionError: #пароль заполнен?
    check ='Вы ввели пустой пароль'
except ValueError: #пароль состоит из цифр?
    check = 'Требования к паролю соблюдены' 
    
print (check)