
B = input("Enter a string (at least two words): ")

words = B.split()

# ����������, �� �������� ������� ����� ��� ��������� �������� ���� (�� ����� 2 �����)
if len(words) > 1:
    # �������� ����� �� ������� �� ��������������� � ����������� �������
    reversed_slice = words[-2::-1]
    result = " ".join(reversed_slice)
    print("Result:", result)
else:
    print("The string is too short to perform a slice operation.")
