# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indices_in_range(arr, min_val, max_val):

    indices = []
    for i in range(len(arr)):
            if min_val <=arr[i] <= max_val:
                indices.append(i)
    
    return indices

numbers = [-5, 9, 0, 3, -1, -2, 1,
 4, -2, 10, 2, 0, -9, 8, 10, -9,
 0, -5, -5, 7]
min_value = 7
max_value = 10
result = find_indices_in_range(numbers, min_value, max_value)
print(f"The indices of elements in the range [{min_value}, {max_value}] are: {result}")
