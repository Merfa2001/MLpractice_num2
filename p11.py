import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'Month': pd.date_range(start='2021-01-01', periods=24, freq='M'),
    'Product A Sales': [500, 480, 600, 750, 900, 850, 920, 1100, 1300, 1350, 1500, 1450, 1550, 1600, 1650, 1600, 1500, 1400, 1600, 1700, 1800, 1750, 1850, 1900],
    'Product B Sales': [300, 320, 400, 450, 500, 580, 700, 750, 820, 900, 950, 980, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1500, 1600, 1550, 1700],
    'Product C Sales': [200, 210, 250, 280, 320, 350, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720]
}

sales_df = pd.DataFrame(data)

# Task 1: Total sales for each product over the two-year period
total_sales = sales_df[['Product A Sales', 'Product B Sales', 'Product C Sales']].sum()
print("Total Sales for Each Product:")
print(total_sales)

# Task 2: Average monthly sales for each product
average_sales = sales_df[['Product A Sales', 'Product B Sales', 'Product C Sales']].mean()
print("\nAverage Monthly Sales for Each Product:")
print(average_sales)

# Task 3: Month with the highest sales for each product
max_sales_month_A = sales_df[sales_df['Product A Sales'] == sales_df['Product A Sales'].max()]['Month'].values[0]
max_sales_month_B = sales_df[sales_df['Product B Sales'] == sales_df['Product B Sales'].max()]['Month'].values[0]
max_sales_month_C = sales_df[sales_df['Product C Sales'] == sales_df['Product C Sales'].max()]['Month'].values[0]
print(f"\nMonth with the Highest Sales for Product A: {max_sales_month_A}")
print(f"Month with the Highest Sales for Product B: {max_sales_month_B}")
print(f"Month with the Highest Sales for Product C: {max_sales_month_C}")

# Task 4: Percentage change in sales from January to December in the second year (2022)
sales_january_2022 = sales_df[sales_df['Month'] == '2022-01-31']
sales_december_2022 = sales_df[sales_df['Month'] == '2022-12-31']
percentage_change_A = ((sales_december_2022['Product A Sales'].values[0] - sales_january_2022['Product A Sales'].values[0]) / sales_january_2022['Product A Sales'].values[0]) * 100
percentage_change_B = ((sales_december_2022['Product B Sales'].values[0] - sales_january_2022['Product B Sales'].values[0]) / sales_january_2022['Product B Sales'].values[0]) * 100
percentage_change_C = ((sales_december_2022['Product C Sales'].values[0] - sales_january_2022['Product C Sales'].values[0]) / sales_january_2022['Product C Sales'].values[0]) * 100
print(f"\nPercentage Change in Sales from January to December 2022 for Product A: {percentage_change_A:.2f}%")
print(f"Percentage Change in Sales from January to December 2022 for Product B: {percentage_change_B:.2f}%")
print(f"Percentage Change in Sales from January to December 2022 for Product C: {percentage_change_C:.2f}%")

# Task 5: Line chart to visualize monthly sales data for each product
plt.figure(figsize=(10, 6))
plt.plot(sales_df['Month'], sales_df['Product A Sales'], label='Product A', marker='o')
plt.plot(sales_df['Month'], sales_df['Product B Sales'], label='Product B', marker='o')
plt.plot(sales_df['Month'], sales_df['Product C Sales'], label='Product C', marker='o')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Data for Each Product (2021-2022)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Task 6: Correlation between Product A and Product B sales
correlation_AB = sales_df['Product A Sales'].corr(sales_df['Product B Sales'])
print(f"\nCorrelation between Product A and Product B Sales: {correlation_AB:.2f}")
# از هوش مصنوعی کمک گرفتم
#done