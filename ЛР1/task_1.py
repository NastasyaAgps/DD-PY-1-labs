numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
summa = 0
k = 0
for i in numbers:
    k += 1
    if i is not None:
        summa += i

sr = summa/k

for a in range(len(numbers)):
    if numbers[a] is None:
        numbers[a] = sr
print("Измененный список:", numbers)
