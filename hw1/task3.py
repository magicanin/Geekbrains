while True:
    num = input("Введите число: ")
    try:
        num=int(num)
        num2=str(num)*2
        num3 = str(num) * 3
        res = int(num)+int(num2)+int(num3)
        print(f"{num}+{num2}+{num3}={res}")
    except Exception as err:
        print(err)
        print("Вы ввели не число - попробуйте ввод снова. Программа не закончит работу, пока вы не введете целое число.")