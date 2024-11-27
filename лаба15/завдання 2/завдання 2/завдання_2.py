import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import calendar

# Зчитуємо дані
data = pd.read_csv("comptagevelo20142.csv")

# Конвертуємо стовпець "Date"
data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y")

# Створюємо графік
plt.figure(figsize=(10, 5))
for column in ["Berri1", "Boyer", "Br?beuf", "CSC (C?te Sainte-Catherine)", "Maisonneuve_2", "Maisonneuve_3",
               "Notre-Dame", "Parc", "PierDup", "Pont_Jacques_Cartier", "Rachel / H?tel de Ville", "Rachel / Papineau",
               "Ren?-L?vesque", "Saint-Antoine", "Saint-Urbain", "Totem_Laurier", "University", "Viger"]:
    plt.plot(data["Date"], data[column], label=column)

plt.title('Загальна популярність велодоріжок за кожен день')
plt.xlabel('Дата')
plt.ylabel('Популярність')

# Змінюємо формат позначень
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

plt.legend()
plt.grid(True)
plt.show()

# Конвертуємо стовпець "Date" та додаємо стовпець місяця
data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y")
data["Month"] = data["Date"].dt.month

# знаходимо найпопулярніший місяць
sum_total = data.groupby("Month")[[
"Berri1", "Boyer", "Br?beuf", "CSC (C?te Sainte-Catherine)", "Maisonneuve_2", "Maisonneuve_3", "Notre-Dame", "Parc", "PierDup",
    "Pont_Jacques_Cartier", "Rachel / H?tel de Ville", "Rachel / Papineau", "Ren?-L?vesque", "Saint-Antoine",
    "Saint-Urbain", "Totem_Laurier", "University", "Viger"]].sum().sum(axis=1)
most_popular_month = sum_total.idxmax()

print(f"\nНайпопулярніший місяць: {most_popular_month} з кількістю : {sum_total.max()}")

