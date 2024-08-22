a = int(input("Enter the value of a (1-100): "))
b = int(input("Enter the value of b (1-100): "))

# Перевірка, чи входять введені значення в діапазон від 1 до 100
if 1 <= a <= 100 and 1 <= b <= 100:
    # Обчислення значення X 
    if a > b:
        X = 2 * a / b + 1
    elif a == b:
        X = -445
    else:  # a < b
        X = (b + 5) / a

    print("The value of X =", X)
else:
    print("Error: a and b must be between 1 and 100.")

