def find_common_products(stores):
    if not stores:
        print("�������� �� ������ ����������.")
        return

    try:
        common_products = set.intersection(*stores)
    except Exception as e:
        print(f"�������: {e}. ������������ ������� � ������.")
        common_products = list(set.intersection(*stores))
        common_products = set(common_products)

    # ��������� ����������
    print("��������, �� � � ��� ���������:", common_products)

def main():
    n = int(input("������ ������� ��������: "))

    stores = []

    # �������� ����������� ������� ��������
    for i in range(n):
        store_products = input(f"������ ���������� �������� {i + 1} ����� �����: ").split()
        store_products_set = set(store_products)  
        stores.append(store_products_set)

    find_common_products(stores)

if __name__ == "__main__":
    main()
