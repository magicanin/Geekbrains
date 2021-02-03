
#print(13+5*60+10*60*60+7*60*60*24)
while True:
    time = input("Введите секунды: ")
    try:
        time=int(time)
        sec=time % 60
        minutes = (time//60)%60
        hours = ((time//60)//60)

        print(f"{hours:02d}:{minutes:02d}:{sec:02d}")

        hours = ((time // 60) // 60) % 24
        days = (((time // 60) // 60) // 24) % 24

        print(f"{days}дн. {hours:02d}:{minutes:02d}:{sec:02d}")

        break
    except:
        print("Вы ввели не секунды - попробуйте ввод снова. Программа не закончит работу, пока вы не введете целое число.")