n = int(input("Введите количество монеток: "))
countA = 0
countB = 0
for i in range(n):
    temp = int(input(f"Введите {i + 1} монетку: "))
    if temp == 0:
        countA += 1
    elif temp == 1:
        countB += 1
print(min(countA, countB))

# Модификация № 1
countC = 0
countD = 0
for i in range(int(input("Введите количество монеток: "))):
    if int(input(f"Введите {i + 1} монетку: ")) == 0:
        countC += 1
    else:
        countD += 1
print(min(countC, countD))

# Модификация № 2
temp = []
for i in range(int(input("Введите количество монеток: "))):
    temp.append(int(input(f"Введите {i + 1} монетку: ")))
print(min(temp.count(0), temp.count(1)))




    


