from random import randint
n = int(input())
numbers = []
for i in range(n):
    numbers.append(randint(-n, n + 1))
print(numbers)


