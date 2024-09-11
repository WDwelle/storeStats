import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import calls

sumOfMoneySpent = calls.salesByAge["sum"]
ageGroup = calls.salesByAge["age"]

# bar graph of spending of each age group
fig, ax = plt.subplots()
ax.bar(ageGroup, sumOfMoneySpent)
ax.set_ylabel('sum of money spent')
ax.set_title('Amount of total money spent by each age group')
plt.show()

# Graphical display to show most popular category by age
age = calls.MostPopularCatByAge["age"]
category = calls.MostPopularCatByAge["category"]

fig, ax = plt.subplots()
ax.bar(age, category)
ax.set_ylabel('Category')
ax.set_title('Most popular category by age')
plt.show()
