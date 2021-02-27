# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
import re

file_name = input("Укажите название файла (c расширением) [file.txt]: ")
try:
    with open(file_name) as myfile:
        line = 0
        words_cnt = 0
        for i in myfile:
            line += 1
            i = re.sub(r'\s+', ' ', i)  # убираем лишние пробелы, если есть
            words = i.split(" ")
            words_cnt += sum(1 for _ in words)
            print(f"{sum(1 for _ in words)} words in line {line}")
        print("\n")
        print(f"Total lines: {line}")
        print(f"Total words: {words_cnt}")

except Exception as err:
    print(err)
