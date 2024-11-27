import pandas as pd

# Початковий словник (лабораторна робота №6)
products_data = {
    "Store": ["Store 1", "Store 1", "Store 2", "Store 2", "Store 3", "Store 3"],
    "Product": ["Apple", "Banana", "Apple", "Orange", "Banana", "Orange"],
    "Quantity": [10, 20, 15, 5, 30, 10],
    "Price": [1.2, 0.8, 1.3, 0.9, 0.85, 0.95]
}

# Перетворення словника на DataFrame
df = pd.DataFrame(products_data)

# Виведення початкового DataFrame
print("Initial DataFrame:")
print(df)

# Додавання нового стовпця "Total Price" (загальна вартість продуктів)
df["Total Price"] = df["Quantity"] * df["Price"]

# Групування даних за магазинами та продуктами, підрахунок загальної кількості та загальної вартості
aggregated = df.groupby(["Store", "Product"]).agg(
    Total_Quantity=pd.NamedAgg(column="Quantity", aggfunc="sum"),
    Total_Revenue=pd.NamedAgg(column="Total Price", aggfunc="sum")
).reset_index()

# Виведення результату групування
print("\nAggregated dataі:")
print(aggregated)

# Групування лише за магазинами, підрахунок загального доходу
store_revenue = df.groupby("Store").agg(
    Total_Revenue=pd.NamedAgg(column="Total Price", aggfunc="sum")
).reset_index()

# Виведення доходу по магазинах
print("\nTotal revenue from shopping:")
print(store_revenue)

