numbers = []
for i in range(4):
  number = float(input(f" Введите число  {i + 1}: "))
  numbers.append(number)

average = sum(numbers) / len(numbers)
print(f"Среднее значение: {average}")