# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

list = []
n = int(input('Введите количество элементов списка: '))
for i in range(n):
    num  = int(input('Введите число: '))
    list.append(num)

x = int(input('Введите искомое число Х: '))
count = 0
for i in list:
    if x == i:
        count+= 1
print(list)
print(count)