# Початкові умови
stipend = 50  
expenses = 80 
total_debt = 0  

# Обчислення боргу за 10 місяців
for month in range(1, 11):
    monthly_debt = expenses - stipend
    total_debt += monthly_debt
    expenses *= 1.02

print("The total debt after 10 months is:", total_debt, "UAH")

