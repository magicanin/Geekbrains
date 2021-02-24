# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint
original_list=[randint(0, 40) for i in range(30)]
print("Исходный список")
print(original_list)
generated_list=[original_list[i] for i in range(0,len(original_list)) if original_list.count(original_list[i])==1]
print("Полученный список ")
print(generated_list)
