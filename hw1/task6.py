#проверяем данные ввода и приводим их к int/float
#если ввели не int и не float - возвращаем False
#
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
    a = is_money(input("Сколько километров спортсмен пробежал в первый день? "))
    b = is_money(input("Какой результат (в километрах) требуется? "))
    result = 1
    if a>0 and b>0 and a<=b:
        while b//a > 0:
            print(f"{result}-й день: {a:.2f}км")
            a *= 1.1
            result+=1
        print(f"{result}-й день: {a:.2f}км")
        print(f"Спортстмен пробежит не менее {b}км на {result}-й день тренировок")
        break
    elif b<a:
        result = 1
        print(f"{result}-й день: {a:.2f}км")
        print(f"Спортстмен пробежит не менее {b}км на {result}-й день тренировок")
        break
    else:
        print(" Вы ввели ошибочные данные - попробуйте ввод снова. \n"
              "Программа не закончит работу, пока Вы не введете положительные числа.")
