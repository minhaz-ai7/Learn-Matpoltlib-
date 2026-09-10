import matplotlib.pyplot as plt
import numpy as np
'''
# x = np.array([2050, 2011, 2022, 2023, 2060])
# y =np.array([20, 12, 26, 29, 30])

months = np.array([1, 2, 3, 4, 5, 6])
revenue = np.array([20, 25, 22, 30, 35, 40])

plt.plot(months , revenue , marker = ".",
                            markersize = 10)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Monthly Revenue")
plt.show()'''


'''study_hours = np.array([1, 2, 3, 4, 5, 6, 7])
score = np.array([20, 30, 40, 50, 60, 70, 80])


plt.scatter(study_hours,score)
plt.xlabel("Study hours")
plt.ylabel("Score")
plt.title("study hours vs exam score")
plt.show()
'''

'''
age = [18, 19, 20, 21, 22, 23]
salary = [15, 18, 22, 25, 30, 35]

plt.scatter(age,salary)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs salary")
plt.show()'''


# bar chart

'''subject = ["english","math","history","ict","statics"]
mark = [65,70,100,87,40]

plt.barh(subject,mark)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()'''


# products = ["Laptop", "Phone", "Tablet", "Watch"]
# sales = [25, 40, 20, 35]

# plt.bar(products,sales)
# plt.xlabel("Products")
# plt.ylabel("Sales")
# plt.title("product sales")
# plt.show()

# ages = [18, 19, 20, 20, 21, 22, 22, 23, 24, 24,
#         25, 25, 26, 27, 28, 29, 30, 30, 31, 32]

# plt.hist(ages , edgecolor = 'black')
# plt.savefig("Matplotlib/ages_chart.png" , dpi = 300)
# plt.show()


# pie chart


'''cate = ["Food", "Rent", "Transport", "Internet"]
expenses = [5000, 8000, 2000, 3000]

plt.pie(expenses ,
        labels= cate,
        autopct="%1.1f%%")
plt.title("Monthly Expenses")
plt.show()'''


# lengend

# months = [1, 2, 3, 4, 5]

# laptop_sales = [10, 15, 12, 20, 25]
# phone_sales = [20, 18, 25, 22, 30]

# plt.plot(months,laptop_sales , label = "Laptop")
# plt.plot(months,phone_sales , label = "Phone")
# plt.legend(loc = "lower center")
# plt.show()


'''months = [1, 2, 3, 4, 5, 6]

product_a = [10, 15, 13, 20, 25, 30]
product_b = [8, 12, 18, 16, 22, 28]


plt.plot(months,product_a , label = "Product A")
plt.plot(months,product_b , label = "Product B")
plt.xlabel("Month")
plt.ylabel("Products")
plt.title("Product A vs B")
plt.legend(loc = "lower right")
plt.show()'''


# subplots
'''x = np.array([1, 2, 3, 4, 5])
fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(x, x*2 , color = "red" )
ax[0,0].set_title("x*2")
ax[0,0].set_xlabel("X axis")
ax[0,0].set_ylabel("Y axis")


ax[0,1].bar(x,x**2 , color = "blue")
ax[0,1].set_title("x**2")
ax[0,1].set_xlabel("X axis")
ax[0,1].set_ylabel("Y axis")


ax[1,0].scatter(x , x**3 , color = "green")
ax[1,0].set_title("x**3")
ax[1,0].set_xlabel("X axis")
ax[1,0].set_ylabel("Y axis")


ax[1,1].plot(x , x**4 , color = "gray")
ax[1,1].set_title("x**4")
ax[1,1].set_xlabel("X axis")
ax[1,1].set_ylabel("Y axis" , color = "red")



plt.tight_layout()
plt.show()
'''


'''fig, ax = plt.subplots(2, 2)

ax[0, 0].plot([1, 2, 3], [10, 20, 15])
ax[0, 1].scatter([1, 2, 3], [20, 15, 25])
ax[1, 0].bar(["A", "B", "C"], [10, 20, 15])
ax[1, 1].hist([10, 12, 15, 15, 18, 20, 20, 22])
plt.tight_layout()
plt.show()'''