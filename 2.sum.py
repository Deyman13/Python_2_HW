num = int(input())
sum = 0
if num > 0:
    for i in range(1, num + 1):
        sum += i
elif num < 0:
    for i in range(1, num - 1, -1):
        sum += i
elif num == 0:
    sum = 1
print(sum)

