password = input('Введите пароль: ')
count = len(password)
mssg="Ваш пароль состоит только из цифр"


try:
    result1 = 10/count 
    result = int(password)
     
except ZeroDivisionError:
    mssg="Вы ввели пустой пароль"    
except ValueError:
    mssg="Требования к паролю соблюдены"

print(mssg)