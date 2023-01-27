"""
Задание 3. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно,
в программе.
Пример:
для списка [5, "string", 0.15, True, None]
результат
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

lst = [5, "string", 0.15, True, None]

for val in lst:
    if type(val) is int:
        print(f'Элемент {val} относится к <class int>')
    elif type(val) is str:
        print(f'Элемент {val} относится к <class str>')
    elif type(val) is float:
        print(f'Элемент {val} относится к <class float>')
    elif type(val) is bool:
        print(f'Элемент {val} относится к <class bool>')
    else:
        print(f'Элемент {val} относится к <class NoneType>')
