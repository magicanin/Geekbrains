str = 'Test string'

bstr = b'test bString'

strnum = '123'

num = int(strnum)


print (f' str: {str}\n',
       f'bstr: {bstr}\n',
       f'strnum: {strnum}\n',
       f'num: {num}')
print(" Если Вы введете вместо строки целое число или число с плавающей точкой - программа выведет ошибку.\n",
      "Программа закончит работу только после ввода строки!")
while True:
    str = input("Введите строку: ");

    stype=type(str)
    try:
        int(str)
        print("Вы ввели число")
    except:
        try:
            float(str)
            print("Вы ввели число с плавающей точкой")
        except:
                print("Вы ввели строку")
                break;
print("Программа закончила работу.")