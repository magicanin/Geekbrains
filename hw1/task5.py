#проверяем данные ввода и приводим их к int/float
#если ввели не int и не float - возвращаем отрицательное число
# (по логике заданий отрицательные значения - не корректные данные)
def is_money(val):
    try:
        int(val)
        return int(val)
    except:
        try:
            float(val)
            return float(val)
        except:
            return -1




while True:
    income = is_money(input("Введите размер выручки: "))
    costs = is_money(input("Введите размер издержек: "))
    if income>=0 and costs>=0:
        if income > costs:
            print(f"Компания сработала с прибылью! Рентабельность {((income-costs)*100/income):.2f}%")
            employees=is_money(input("Укажите количество сотрудников компании: "))
            if(employees>0):
                print(f"Средняя прибыль на сотрудника составила {((income-costs)/employees):.2f}")
            else:
                print(f"Среднюю прибыль на сотрудника не посчитать, если не вводить корректные данные )")
        elif income < costs:
            print(f"Компания показала убыток {income-costs}.")
        else:
            print("Компания сработала в ноль")
        break
    else:
        print("Вы ввели ошибочные данные - попробуйте ввод снова. Программа не закончит работу, пока вы не введете положительные числа или 0.")