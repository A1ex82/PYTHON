n = int(input('Введите количество монет: '))
head = 0
tail= 0
for i in range(n):
    coin = int(input("Введите строну монеты: "))
    if coin == 1:
        head += 1
    elif coin == 0:
        tail += 1
if head > tail:
    print(tail)
else: print(head) 