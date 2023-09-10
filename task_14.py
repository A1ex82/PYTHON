N = int(input("Введите число (N): "))
for i in range(N + 1):
    power_of_two = 2 ** i
    if 2 ** i <= N:
        print(power_of_two)
    else:
        break