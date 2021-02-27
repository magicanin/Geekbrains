# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from statistics import mean

try:
    with open("employees.txt") as myfile:
        workers = myfile.readlines()
        print(workers)
        empl = list()
        for worker in workers:
            employee, salary = worker.split()
            salary: int = int(salary)
            if salary < 20000:
                print(f"Зарплата {employee}: {salary}")
            empl.append(salary)
        print(f"Средняя зарплата: {mean(empl)}")
except Exception as err:
    print(err)