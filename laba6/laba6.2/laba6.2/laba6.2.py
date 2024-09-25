def find_common_products(stores):
    if not stores:
        print("Магазини не надали асортимент.")
        return

    try:
        common_products = set.intersection(*stores)
    except Exception as e:
        print(f"Помилка: {e}. Перетворюємо множину в список.")
        common_products = list(set.intersection(*stores))
        common_products = set(common_products)

    # Виведення результату
    print("Продукти, які є в усіх магазинах:", common_products)

def main():
    n = int(input("Введіть кількість магазинів: "))

    stores = []

    # Введення асортименту кожного магазину
    for i in range(n):
        store_products = input(f"Введіть асортимент магазину {i + 1} через пробіл: ").split()
        store_products_set = set(store_products)  
        stores.append(store_products_set)

    find_common_products(stores)

if __name__ == "__main__":
    main()
