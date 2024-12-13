num = range(1, 20)
number_1 = int(input("Введите число: " ))
pairs = []
for i in range(len(num)):
    for j in range(i+1, len(num)):
        sum_num = num[i] + num[j]
        if number_1 % sum_num == 0:
            pairs.append((num[i], num[j]))
for result in pairs:
    print(result)

