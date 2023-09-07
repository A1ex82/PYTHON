N = int(input("Введите число (N): "))
for i in range(N + 1):
    total = 2 ** i
    if 2 ** i <= N:
        print(total)
    else:
        break