# Реализуйте функцию custom_filter(), которая на вход принимает список some_list,
# с любыми типами данных, находит в этом списке целые числа, отбирает из них те,
# что делятся нацело на 7, суммирует их, а затем проверяет превышает эта сумма 83 или нет.
# Если НЕ превышает - функция должна вернуть True, если превышает - False.
#
# Примечание. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию custom_filter(), но не код, вызывающий ее.
#
# some_list = [7, 14, 28, 32, 32, 56]
#
# print(custom_filter(some_list))

# def custom_filter(some_list: list, sum: int=0, criteria: int=83) -> bool:
#     for elem in some_list:
#         if type(elem) == int and elem % 7 == 0:
#                 sum+=elem
#     return not sum>criteria

# def custom_filter(some_list):
#     return sum(filter(lambda x: type(x)==int and x%7==0, some_list))<83
#
# my_list: list=[]
# my_list = [7, 14, 28, 32, 32, 56]
# #my_list = [7, 14, 28, 32, 32, '56']
#
# print(custom_filter(my_list))

#counter = test_str.count('t')

# def custom_filter(some_list):
#     return sum(filter(lambda x: type(x)==int and x%7==0, some_list))<83

# anonimous_filter = lambda x: (x.count('я') + x.count('Я'))>=23
# #
# print(anonimous_filter('последняя буква в алфавите Я - !'))
#
# print(anonimous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))

# class MyClass:
#     def __init__(self) -> None:
#         pass
#
#     def __call__(self) -> str:
#         return 'Результат вызова экземпляра класса'
#
# my_class_1 = MyClass()
# my_class_2 = MyClass()
#
# print(my_class_1())
# print(my_class_2())

from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message











