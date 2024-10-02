# Функція для виведення всіх значень словника
def print_teams(teams):
    print("\nКоманди та їх очки:")
    for team, points in teams.items():
        print(f"{team}: {points} очок")
    print()

# Функція для додавання нового запису до словника
def add_team(teams):
    team_name = input("Введіть назву команди: ")
    points = int(input("Введіть кількість очок: "))
    if team_name in teams:
        print("Команда вже існує. Спробуйте ще раз.")
    else:
        teams[team_name] = points
        print(f"Команду '{team_name}' успішно додано!")

# Функція для видалення запису зі словника
def remove_team(teams):
    team_name = input("Введіть назву команди для видалення: ")
    if team_name in teams:
        del teams[team_name]
        print(f"Команду '{team_name}' успішно видалено!")
    else:
        print("Команди не знайдено. Спробуйте ще раз.")

# Функція для перегляду вмісту словника за відсортованими ключами
def view_sorted_teams(teams):
    sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True)
    print("\nКоманди за очками (від найвищих до найнижчих):")
    for team, points in sorted_teams:
        print(f"{team}: {points} очок")
    print()

# Функція для визначення чемпіона та призерів
def find_top_teams(teams):
    sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True)
    champion = sorted_teams[0][0]
    second_place = sorted_teams[1][0]
    third_place = sorted_teams[2][0]
    print(f"Чемпіон: {champion}")
    print(f"Друге місце: {second_place}")
    print(f"Третє місце: {third_place}\n")

# Головна функція для роботи зі словником
def main():
    # Ініціалізація словника з даними про команди
    teams = {
        "Команда А": 30,
        "Команда Б": 24,
        "Команда В": 18,
        "Команда Г": 15,
        "Команда Д": 10,
        "Команда Е": 8,
        "Команда Ж": 7,
        "Команда З": 6,
        "Команда И": 5,
        "Команда Й": 4
    }

    while True:
        print("\nМеню:")
        print("1. Вивести всі команди")
        print("2. Додати команду")
        print("3. Видалити команду")
        print("4. Переглянути команди за очками")
        print("5. Визначити чемпіона та призерів")
        print("6. Вийти")

        choice = input("Виберіть опцію (1-6): ")
        
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
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

