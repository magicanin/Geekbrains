# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_func(a: int,b: int)->float:
    try:
        return a/b
    except ZeroDivisionError:
        print("Ошибка деления на ноль")
        return False

def prepare_to_division(a):
    try:
        int(a)
        return int(a)
    except ValueError:
        try:
            float(a)
            return float(a)
        except ValueError:
            return "Not Digit"
    except Exception as err:
        print(err)
        return "Not Digit"

while True:
    a=prepare_to_division(input("Введите значение переменной a: "))
    b=prepare_to_division(input("Введите значение переменной b: "))
    continue_var='n'
    if a!="Not Digit" and b!="Not Digit":
        print(division_func(a,b))
    else:
        continue_var=input("Вы ввели не корректные значения. Чтобы повторить попытку - введите 'У': ")
        if continue_var.lower()!='y':
            break
    if continue_var.lower()!='y' and input("Для выхода из программы введите 'quit' для продолжения - нажмите enter: ").lower() == 'quit':
        break