number = float(input("1 способ. Введите число: "))
number *= 10000
sum1 = 0
while number != 0:
    sum1 += number % 10
    number //= 10
print(f'Сумма всех цифр в числе = {int(sum1)}')


sum2 = 0
for i in list(input("2 способ. Введите число: ").replace(".", "")):
    sum2 += int(i)
print(f'Сумма всех цифр в числе = {int(sum2)}')


print(f'Сумма всех цифр в числе = {sum(map(int, input("3 способ. Введите число: ").replace(".", "")))}')


    


