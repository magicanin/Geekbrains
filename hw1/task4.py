while True:
    num = input("Введите число: ")
    try:
        num=int(num)
        numstr = num
        res = 0
        while num > 0:
            tmp = num % 10
            num //= 10
            if tmp > res:
                res = tmp
        print(f"В числе {numstr} максимальная цифра {res}")
        break
    except Exception as err:
        print(err)
        print("Вы ввели не число - попробуйте ввод снова. Программа не закончит работу, пока вы не введете целое число.")