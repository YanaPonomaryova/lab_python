def add_odd_index_elements(lst):
    # ��������� ����� ������ � ��������, �� ����� ������ �������
    odd_index_elements = [lst[i] for i in range(1, len(lst), 2)]
    lst.extend(odd_index_elements)
    # ���������
    print("������������ ������:", lst)
def main():
    lst = input("������ �������� ������ ����� �����: ").split()
    lst = [int(x) for x in lst]
    add_odd_index_elements(lst)
if __name__ == "__main__":
    main()

