# Введення даних користувачем
N = int(input("Enter the number of elements in the array: "))
arr = []

print("Enter the elements of the array:")
for i in range(N):
    element = float(input(f"Element {i+1}: "))
    arr.append(element)

# Обчислення середнього арифметичного непарних елементів
odd_elements = [x for x in arr if x % 2 != 0]  
if odd_elements:
    average_odd = sum(odd_elements) / len(odd_elements)
    print(f"Arithmetic mean of odd elements: {average_odd}")
else:
    print("No odd elements.")
    
# Виведення від'ємних елементів у зворотному порядку
negative_elements = [x for x in arr if x < 0]
if negative_elements:
    print("Negative elements in reverse order:", negative_elements[::-1])
else:
    print("No negative elements.")
