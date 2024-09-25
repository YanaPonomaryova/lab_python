def find_surrounding_elements(lst, element):
    
    if element not in lst:
        print("Заданий елемент відсутній у списку.")
        return

    # Знаходимо індекс елемента
    index = lst.index(element)

    # Знаходимо оточуючі елементи
    left = lst[index - 1] if index > 0 else None 
    right = lst[index + 1] if index < len(lst) - 1 else None  

    # Друкуємо результат
    print(f"Елемент: {element}")
    if left is not None:
        print(f"Лівий сусід: {left}")
    else:
        print("Лівий сусід: відсутній (елемент на початку списку)")

    if right is not None:
        print(f"Правий сусід: {right}")
    else:
        print("Правий сусід: відсутній (елемент в кінці списку)")

def main():
    # Введення списку з клавіатури
    lst = input("Введіть елементи списку через пробіл: ").split()
    lst = [int(x) for x in lst]  # Перетворюємо введені дані у список чисел

    # Введення елемента для пошуку
    element = int(input("Введіть елемент, оточуючі елементи якого треба знайти: "))

    find_surrounding_elements(lst, element)

if __name__ == "__main__":
    main()

