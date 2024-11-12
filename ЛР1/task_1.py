numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
valid_numbers = numbers[:4] + numbers[5:]
summa = sum(valid_numbers)
k = len(numbers)
sr = summa/k
numbers = numbers[:4] + [sr] + numbers[5:]
print("Измененный список:", numbers)

