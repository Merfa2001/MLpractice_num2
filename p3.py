import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May']
sales = [5000, 6000, 7500, 8000, 7000]

plt.bar(months, sales, color='skyblue')
plt.xlabel('Month')
plt.ylabel('Sales (in USD)')
plt.title('Monthly Sales for the Store (January to May)')

plt.show()
#done