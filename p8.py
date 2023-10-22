import pandas as pd

data = {
    'Product Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A'],
    'Sales Amount': [100, 200, 150, 300, 250, 180, 120]
}

sales_data = pd.DataFrame(data)

total_sales_per_category = sales_data.groupby('Product Category')['Sales Amount'].sum()

print(total_sales_per_category)
#done