import matplotlib.pyplot as plt

years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
population = [50000, 55000, 60000, 65000, 70000, 72000, 75000, 78000, 80000, 82000]

plt.plot(years, population, marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('City Population Growth Over 10 Years')

plt.grid(True)
plt.show()
#done