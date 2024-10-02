# ������� ��� ��������� ��� ������� ��������
def print_teams(teams):
    print("\n������� �� �� ����:")
    for team, points in teams.items():
        print(f"{team}: {points} ����")
    print()

# ������� ��� ��������� ������ ������ �� ��������
def add_team(teams):
    team_name = input("������ ����� �������: ")
    points = int(input("������ ������� ����: "))
    if team_name in teams:
        print("������� ��� ����. ��������� �� ���.")
    else:
        teams[team_name] = points
        print(f"������� '{team_name}' ������ ������!")

# ������� ��� ��������� ������ � ��������
def remove_team(teams):
    team_name = input("������ ����� ������� ��� ���������: ")
    if team_name in teams:
        del teams[team_name]
        print(f"������� '{team_name}' ������ ��������!")
    else:
        print("������� �� ��������. ��������� �� ���.")

# ������� ��� ��������� ����� �������� �� ������������� �������
def view_sorted_teams(teams):
    sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True)
    print("\n������� �� ������ (�� �������� �� ���������):")
    for team, points in sorted_teams:
        print(f"{team}: {points} ����")
    print()

# ������� ��� ���������� ������� �� �������
def find_top_teams(teams):
    sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True)
    champion = sorted_teams[0][0]
    second_place = sorted_teams[1][0]
    third_place = sorted_teams[2][0]
    print(f"������: {champion}")
    print(f"����� ����: {second_place}")
    print(f"���� ����: {third_place}\n")

# ������� ������� ��� ������ � ���������
def main():
    # ����������� �������� � ������ ��� �������
    teams = {
        "������� �": 30,
        "������� �": 24,
        "������� �": 18,
        "������� �": 15,
        "������� �": 10,
        "������� �": 8,
        "������� �": 7,
        "������� �": 6,
        "������� �": 5,
        "������� �": 4
    }

    while True:
        print("\n����:")
        print("1. ������� �� �������")
        print("2. ������ �������")
        print("3. �������� �������")
        print("4. ����������� ������� �� ������")
        print("5. ��������� ������� �� �������")
        print("6. �����")

        choice = input("������� ����� (1-6): ")
        
        if choice == '1':
            print_teams(teams)
        elif choice == '2':
            add_team(teams)
        elif choice == '3':
            remove_team(teams)
        elif choice == '4':
            view_sorted_teams(teams)
        elif choice == '5':
            find_top_teams(teams)
        elif choice == '6':
            print("����� � ��������.")
            break
        else:
            print("������������ ����. ��������� �� ���.")

if __name__ == "__main__":
    main()

