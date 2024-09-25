def add_odd_index_elements(lst):
    # Створюємо новий список з елементів, що мають непарні індекси
    odd_index_elements = [lst[i] for i in range(1, len(lst), 2)]
    lst.extend(odd_index_elements)
    # Результат
    print("Результуючий список:", lst)
def main():
    lst = input("Введіть елементи списку через пробіл: ").split()
    lst = [int(x) for x in lst]
    add_odd_index_elements(lst)
if __name__ == "__main__":
    main()

