import os
os.system('cls')

# Задача 1. Множественная форма числительных

correct_form = None


def plural_form(a,form_1,form_2,form_3):
    """Подбор множественной формы существительного в зависимости от числительного
    :param a: числительное
    :param form_1: первая форма
    :param form_2: вторая форма
    :param form_3: третья форма"""

    if a % 10 == 1 and a % 100 != 11:
        correct_form = form_1
    elif a % 10 in range(2, 5) and a % 100 not in range(12, 15):
        correct_form = form_2
    else:
        correct_form = form_3
    
    return (correct_form)


print()
print(f"3 {plural_form(3,'яблоко','яблока','яблок')}")
print(f"15 {plural_form(15,'студент','студента','студентов')}")
print ('================================================')

# Задача 2. FizzBuzz

sum = 0

for i in range(1000, 20001):
    if i%3 == 0 and i%5 == 0:
        sum += i

print (f'сумма чисел в задаче FizzBuzz = {sum}')
print ('================================================')


# Задача 3. Последовательность Фибоначчи

fib1 = fib2 = 1

n1_count = 1 # счётчик кол-ва чисел в последовательности
n2_sum = 0 # счётчик суммы чётных чисел
n3_even = [] # список чётных чисел последовательности
n4_fib_list = [] # список чисел последовательности
 
while fib2 < 10000000:
    fib1, fib2 = fib2, fib1 + fib2
    n1_count +=1
    n4_fib_list.append(fib1)

    if fib1 % 2 == 0:
        n2_sum += fib1
        n3_even.append(fib1)

print (f'количество элементов = {n1_count}')
print (f'сумма чётных элементов = {n2_sum}')
print (f'чётные элементы = {n3_even}')
print (f'предпоследнее число = {n4_fib_list[-2]}')