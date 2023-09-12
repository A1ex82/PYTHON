# Ввод количества элементов в первом и втором множестве
n = int(input("Введите количество элементов в первом множестве: "))
m = int(input("Введите количество элементов во втором множестве: "))

# Ввод элементов первого множества
set1 = set()
print("Введите элементы первого множества:")
for i in range(n):
    element = int(input())
    set1.add(element)

# Ввод элементов второго множества
set2 = set()
print("Введите элементы второго множества:")
for i in range(m):
    element = int(input())
    set2.add(element)

# Находим пересечение множеств (числа, которые встречаются в обоих множествах)
intersection = set1.intersection(set2)

# Преобразуем результат в список и сортируем его
result = list(intersection)
result.sort()

if len(intersection) == 0:
    print("Множества не имеют пересечений.")
else:
    print(f"Числа, которые встречаются в обоих множествах и отсортированы по возрастанию:")
    print(*result)
# for number in result:
#     print(number)
