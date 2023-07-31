
# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# progr = []
# progr.append(int(input('vvedite pervoe chislo: ')))
# d = int(input("vvedite raznost' elementov: "))
# kol = int(input("kolichestvo elementov: "))

# for i in range(1,kol):
#     an=progr[0] + i * d
#     progr.append(an)

# for i in range(kol):
#     print(f"Элемент {i+1} прогрессии равен {progr[i]}")


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

mass = []
ind = []
kol = int(input("Vvedite kolichestvio elementov massiva: "))
a = int(input("vvedite start diap elementov: "))
b = int(input("vvedite end diap elementov: "))

for i in range(0, kol):
    an = random.randint(0, 30)
    mass.append(an)

for i in range(0, kol):
    print(f"Элемент {i} прогрессии равен {mass[i]}")

for i in range(0, kol):
    if (mass[i] <=b and mass[i]>=a):
        ind.append(i)

for i in range(len(ind)):
    print(f"{ind[i]}  ")