def find_surrounding_elements(lst, element):
    
    if element not in lst:
        print("������� ������� ������� � ������.")
        return

    # ��������� ������ ��������
    index = lst.index(element)

    # ��������� �������� ��������
    left = lst[index - 1] if index > 0 else None 
    right = lst[index + 1] if index < len(lst) - 1 else None  

    # ������� ���������
    print(f"�������: {element}")
    if left is not None:
        print(f"˳��� ����: {left}")
    else:
        print("˳��� ����: ������� (������� �� ������� ������)")

    if right is not None:
        print(f"������ ����: {right}")
    else:
        print("������ ����: ������� (������� � ���� ������)")

def main():
    # �������� ������ � ���������
    lst = input("������ �������� ������ ����� �����: ").split()
    lst = [int(x) for x in lst]  # ������������ ������ ��� � ������ �����

    # �������� �������� ��� ������
    element = int(input("������ �������, �������� �������� ����� ����� ������: "))

    find_surrounding_elements(lst, element)

if __name__ == "__main__":
    main()

