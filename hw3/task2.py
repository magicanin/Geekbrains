# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def set_profile(name, familyname, birth_year, city, email, phone):
    print(f"{name} {familyname} lives in {city}, was born in {birth_year}. Contacts: {email}, {phone}")

set_profile(familyname='Mironov', name='Mikhail', birth_year="1985", city="Moscow",
            phone="79261234567", email="i@mmironov.ru")