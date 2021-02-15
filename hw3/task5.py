# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

SPECIAL_CHAR="N"


def validate_data(x):
    try:
        x=float(x)
        return x
    except Exception as err:
        print(err)
        print("Введены не корректные данные.")
    if SPECIAL_CHAR in x or x == SPECIAL_CHAR:
        print("Введен специальный символ.")
        return "Stop input"
    return 0

global rslt

rslt=0

def parse_input(sdata):
    sdata=sdata.split(" ")
    sum=0
    global rslt
    for data in sdata:
        rslt=validate_data(data)
        if rslt != "Stop input":
             sum+=rslt
        else:
            break
    return sum


sum=0
while rslt!="Stop input":
    sdata=input("Введите строку чисел, разделенных пробелом: ")
    print(f"Для прекращения ввода строка должна содержать '{SPECIAL_CHAR}'")
    sum+=parse_input(sdata)

print("Сумма введенных чисел равна: ", sum)


