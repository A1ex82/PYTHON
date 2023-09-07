S = int(input("Введите сумму (S): "))
P = int(input("Введите произведение (P): "))

for X in range(1, S):
    Y = S - X 
    if X * Y == P:
        print(X, Y)