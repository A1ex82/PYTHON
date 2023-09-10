# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

list = []
n = int(input('Введите количество элементов списка: '))
for i in range(n):
    num  = int(input('Введите число: '))
    list.append(num)
x = int(input('Введите искомое число Х: '))
num_min = list[0]
dif_min = abs(x - list[0])
for num in list:
    dif = abs(x - num)
    if dif < dif_min:
        dif_min = dif
        num_min = num
print(list)
print(num)