# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count

def get_digit(n):
     try:
          n = int(n)
          return n
     except ValueError:
          print("Введённый символ не является числом!!!")
          return 'Error'


def my_fun_count(start=0, stop=10,my_list=[]) ->list:
     """
     start=0 - число — стартового параметра
     stop=20 - количество генерируемых чисел
     my_list=[] - список сгенерированных чисел

     Функция генерирующая целые числа, начиная с указанного;
     """
     iter=count(start)
     for i in range(0,stop-start+1):
         my_list.append(next(iter))
     return my_list

from itertools import cycle

def my_fun_cycle(my_list=[]) ->list:
     """
     my_list=[] - список сгенерированных чисел

     Функция повторяющая элементы некоторого списка, определённого заранее;
     """
     iter=cycle(my_list)
     my_list_double=[]
     for i in range(0,len(my_list)):
         my_list_double.append(next(iter))
     return my_list_double

a=get_digit(input("C какого числа начать генерацию? "))
b=get_digit(input("До какого числа генерировать? "))
if a!="error" and b!="error" and a < b:
     print(f"Генерируем целые числа, начиная с {a} по {b}")

     my_list=my_fun_count(start=a, stop=b)
     print(my_list)
     print("Повторяем элементы списка, определённого заранее")
     my_list_double=my_fun_cycle(my_list)
     print(my_list_double)
else:
     print("Введены не верные данные!")