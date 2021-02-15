# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

import re

def only_letters(tested_string):
    match = re.match("^[a-z]*$", tested_string)
    return match is not None

def my_capitalize(word):
    return word[0].upper()+word[1:] 

def re_capitalize(word):
    return word.capitalize()

def man_capitalize(word):
    return chr(ord(word[0])-32) + word[1:]

continueflag="Y"
while continueflag !="N":
    test=input("Введите слово из маленьких латинских букв: ")
    if only_letters(test) == True:
        print("var[0].upper()     : ", my_capitalize(test))
        print("var.capitalize()   : ", re_capitalize(test))
        print("chr(ord(var[0])-32): ",man_capitalize(test))
    else:
        print("Веедены ошибочные данные")
    continueflag = input("Продолжить? Y/N: ")