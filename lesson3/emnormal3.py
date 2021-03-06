# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

name = ["masha", "vlad", "katya", "sveta", "sasha"]
salary = ["60000", "135000", "45000", "50000", "600000"]
dict_salary = dict(zip(name, salary))

with open("salary.txt", "w") as out:
    for a, b in dict_salary.items():
        print(f"{a} - {b}", file=out)

f = open('salary.txt')

for line in f:
    salary_item = int(line.split()[2])
    salary_new = int(salary_item * 0.87)
    name = line.split()[0].upper()
    if salary_item < 500000:
        print(name, salary_new)
