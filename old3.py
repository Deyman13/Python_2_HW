n = int(input('Введите число: '))
templist = []
for n in range(1, n + 1):
    templist.append(round((1 + 1 / n)**n, 2))
print(f'{templist}\n', sum(templist))





