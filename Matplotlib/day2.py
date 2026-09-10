import matplotlib.pyplot as plt
import numpy as np 

'''
months = [1, 2, 3, 4, 5]

sales = [10, 15, 12, 20, 25]
profit = [3, 5, 4, 7, 9]

products = ["A", "B", "C"]
product_sales = [20, 35, 25]

ages = [18, 19, 20, 20, 21, 22, 22, 23, 24, 25]


fig , axis = plt.subplots(2,2)
axis[0,0].plot(sales)

axis[0,1].scatter(sales,profit)

axis[1,0].bar(products,product_sales)

axis [1,1].hist(ages)
plt.show()'''


# days = [1, 2, 3, 4, 5]
# sales = [10, 15, 12, 20, 25]

# plt.figure(figsize=(8,10))

# plt.plot(days, sales, color="#8c1f73",
#                       marker = "o",
#                       linestyle = ":",
#                       linewidth = 2,
#                       markersize = 2) 
# plt.grid(axis="both")
# plt.show()


'''months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
profit = [12, 18, 15, 22, 28, 32]

plt.figure(figsize=(10,5))

plt.plot(months,profit , color = "#c99d0c",
                        marker = "*",
                        linestyle = ":",
                        linewidth = 3,
                        markersize = 7,
                        alpha = 1)


plt.grid()
plt.xlabel("Months" , color = "#dab12a")
plt.ylabel("Profit" , color = "#cf0819")
plt.title("months vs profit" , color = "#1eb023")
plt.show()
'''


# days = [1, 2, 3, 4, 5]
# sales = [10, 15, 12, 20, 25]

# plt.plot(days, sales)

# plt.xlabel("Day")
# plt.ylabel("Sales")
# plt.title("Daily Sales")

# plt.xlim(1, 100)
# plt.ylim(0, 20)

# plt.grid()

# plt.show()



import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [10, 15, 12, 20, 25]

plt.plot(days, sales, marker="o")

plt.annotate(
    "Highest Sales",
    xy=(5, 25),
    xytext=(3.5, 27),
    arrowprops=dict(arrowstyle="->")
)

plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Daily Sales")

plt.show()