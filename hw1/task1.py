checkstring = 'Test string'

bstr = b'test bString'

strnum = '123'

num = int(strnum)


print (f' str: {checkstring}\n',
       f'bstr: {bstr}\n',
       f'strnum: {strnum}\n',
       f'num: {num}')
print(" Если Вы введете вместо строки целое число или число с плавающей точкой - программа выведет ошибку.\n",
      "Программа закончит работу только после ввода строки!")
while True:
    checkstring = input("Введите строку: ");

    stype=type(checkstring)
    try:
        int(checkstring)
        print("Вы ввели число")
    except ValueError as err:
        print(err)
        try:
            float(checkstring)
            print("Вы ввели число с плавающей точкой")
        except Exception as err:
            print(err)
            print("Вы ввели строку")
            break;
print("Программа закончила работу.")