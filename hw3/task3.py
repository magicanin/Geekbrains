# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
   try:
        return sum([a,b,c])-min(a,b,c)
   except Exception as err:
        print(f"Ошибка: {err}")

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

continueflag="Y"
while continueflag !="N":
    a=prepare_to_division(input("Введите a: "))
    b=prepare_to_division(input("Введите b: "))
    c=prepare_to_division(input("Введите c: "))

    print("Сумма двух максимальных переменных:",my_func(a,b,c))
    continueflag = input("Продолжить? Y/N: ")