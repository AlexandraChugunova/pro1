# словари для хранения данных об аккаунтах
account1 = {'login':'Ivan','password':'q1'}
account2 = {'login':'Petr','password':'q2'}
account3 = {'login':'Olga','password':'q3'}
account4 = {'login':'Anna','password':'q4'}

# словари с данными о пользователях
user1 = {'name':'Иван','age':20,'account':account1}
user2 = {'name':'Пётр','age':25,'account':account2}
user3 = {'name':'Ольга','age':18,'account':account3}
user4 = {'name':'Анна','age':27,'account':account4}

# список пользователей
user_list = [user1, user2, user3, user4]

# ЗАДАЧА 1

# ввод ключа пользователем
# перевод введённого ключа в нижний регистр
key_input = (input ('Введите ключ: ')).lower()

i=0 # объявление переменной цикла
# цикл, выводящий данные о пользователях по ключам
while i<= len(user_list[-1]): # индекс связан с длиной строки; определяем i через длину
    # поиск введённого пользователем ключа
    # в словаре элемента с индексом i
    # списка user_list
    key = user_list[i].get(key_input,'Введённый ключ не найден')
    result = f'Значение ключа {key_input} для user{i+1} = {key}'
    print (result)
    i=i+1

# ЗАДАЧА 2

# ввод порядкового номера пользователем
# здесь и далее считаем, что нумерация пользователей при вводе с 1 (не с 0)
user_number = int(input("\n" + 'Введите порядковый номер: '))

# проверка существования пользователя с данным номером
# вывод имени, возраста, логина и пароля пользователя с user_number
if (user_number - 1) > len(user_list[-1]):
    print ('Пользователь с указанным номером не найден')
else:
   data = f'Данные по пользователю №{user_number}:'
   name = f"Имя:{user_list[user_number-1].get('name',0)}"
   age = f"Возраст:{user_list[user_number-1].get('age',0)}"
   login = f"Логин:{user_list[user_number-1].get('account',0).get('login',0)}"
   password = f"Пароль:{user_list[user_number-1].get('account',0).get('password',0)} "
   print (data)
   print (name)
   print (age)
   print (login)
   print (password)

# ЗАДАЧА 3

# ввод номера пользователя, которого нужно переместить в конец
user_end = int(input("\n" + 'Введите номер пользователя, которого нужно переместить в конец: '))

if (user_end - 1) > len(user_list[-1]):
    print ('Пользователь с указанным номером не найден')
else:
    print ('Список до изменения: \n {}'.format(user_list)) # вывод списка до изменения (исходного)
    end = user_list.pop(user_end-1) # извлечение перемещаемого элемента
    user_list.append(end) # добавление в список перемещаемого элемента
    print ('Пользователь с именем {} перемещён в конец'.format(user_list[user_end].get('name',0)))
    print ('Список после изменения: \n {}'.format(user_list))

# ЗАДАЧА 4

from statistics import mean

avg_age = [] # создание список возрастов пользователей
j=0 # объявление переменной цикла

# цикл, наполняющий список avg_age
while j<= len(user_list[-1]): # индекс связан с длиной строки; определяем j через длину
    add_age = user_list[j].get('age',0)
    avg_age.append(add_age)
    j=j+1

avarage = mean(avg_age) # вычисление среднего возраста пользователей
print ("\n" + 'Средний возраст пользователей: {}'.format(avarage))