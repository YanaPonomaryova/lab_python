
B = input("Enter a string (at least two words): ")

words = B.split()

# Перевіряємо, чи достатня довжина рядка для виконання операції зрізу (як мінімум 2 слова)
if len(words) > 1:
    # Отримуємо слова від першого до передостаннього у зворотньому порядку
    reversed_slice = words[-2::-1]
    result = " ".join(reversed_slice)
    print("Result:", result)
else:
    print("The string is too short to perform a slice operation.")
