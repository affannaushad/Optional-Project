# Affan Naushad
# 501047523
# Optional Project

import csv
import matplotlib.pyplot as plt

# Step 1: Reading CSV File
with open('data.csv', mode='r') as fileCSV:
    data = list(csv.reader(fileCSV))

    
    for line in data:
        print(line)

# Step 2: Total Sale
with open('stats.txt', mode='w') as stats_file:
    stats_file.write("Year,Total Sales\n")

    for year in range(2012, 2022):
        total_sales = sum(int(row[month]) for row in data[1:] for month in range(1, 13) if row[0].startswith(str(year)))
        stats_file.write(f"{year},{total_sales}\n")

# Step 3: Bar Plot
x = [str(year) for year in range(2012, 2022)]
y = [sum(int(row[month]) for row in data[1:] for month in range(1, 13) if row[0].startswith(str(year))) for year in range(2012, 2022)]

plt.figure()
plt.bar(x, y)

plt.title("Total Sales by Year")
plt.xlabel("Year")
plt.ylabel("Total Sales")

plt.show()

# Step 4: Sale Estimation
sales_2021 = sum(int(row[month]) for row in data[1:] for month in range(1, 7) if row[0].startswith("2021"))
sales_2022 = sum(int(row[month]) for row in data[1:] for month in range(1, 7) if row[0].startswith("2022"))
sales_growth_rate = (sales_2022 - sales_2021) / sales_2021

with open('stats.txt', mode='a') as stats_file:
    stats_file.write(f"Sales Growth Rate,{sales_growth_rate}\n")
    stats_file.write("Month,Estimated Sales in 2022\n")

    for month in range(7, 13):
        sales_2021_month = sum(int(row[month]) for row in data[1:] if row[0].startswith("2021"))
        estimated_sales_2022_month = sales_2021_month + sales_2021_month * sales_growth_rate
        stats_file.write(f"{month},{estimated_sales_2022_month}\n")

# Step 5: Horizontal Bar Plot
x = [f"Month {month}" for month in range(7, 13)]
y = [sum(int(row[month]) for row in data[1:] for month in range(1, 13) if row[0].startswith("2022")) for month in range(7, 13)]

plt.figure()
plt.barh(x, y)

plt.title("Estimated Sales in Second Half of 2022")
plt.xlabel("Total Sales")
plt.ylabel("Month")

plt.show()
