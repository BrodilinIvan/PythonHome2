"""
Урок 2. Циклы (for, while)
Задание 1.
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

km_first_day = float(input('Укажите километраж первого дня - '))
km_rezult_day = float(input('Укажите требуемый результат в км - '))


def func_sport(a, b):
    day = 1
    print('Результат:')
    print(f'{day}-й день: {a}')
    while a < b:
        a += a / 10
        day += 1
        print(f'{day}-й день: {a:.2f}')
    return day


print(f'Ответ: на {func_sport(km_first_day, km_rezult_day)}-й день спортсмен '
      f'достиг результата - не менее {km_rezult_day} км')