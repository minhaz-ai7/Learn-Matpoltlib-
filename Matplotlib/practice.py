'''



🔥 কোন মাসে highest sales?
📉 কোন মাসে lowest sales?'''

import pandas as pd
import matplotlib.pyplot as plt


#1 📈 Monthly sales trend কেমন?
df = pd.read_csv("Matplotlib/sales.csv")
df["Date"] = pd.to_datetime(df["Date"])


# # print(df.head())
# # print(df.shape)
# # print(df.info())
# # print(df.describe())

# df["Month"] = df["Date"].dt.month_name()

# # print(df[["Date", "Month", "Sales"]])


# monthly_sales = df.groupby("Month")["Sales"].sum()


# plt.figure(figsize=(10,5))
# plt.plot(monthly_sales.index,
#          monthly_sales.values,
#          marker = "o",
#          linewidth = 2)

# plt.xlabel("Month")
# plt.ylabel("Total Sales")
# plt.title("Monthly Sales Trend")
# plt.grid(axis= "y")
# plt.tight_layout()



# #2💰 কোন category সবচেয়ে বেশি revenue করেছে?
# category_sales = df.groupby("Category")["Sales"].sum()
# plt.figure(figsize=(8,5))
# plt.bar(category_sales.index,
#          category_sales.values)
# plt.xlabel("Categorys")
# plt.ylabel("Total Sales")
# plt.title("Sales by Category")
# plt.grid(axis="y")
# plt.tight_layout()



# #3 🏆 কোন product সবচেয়ে বেশি বিক্রি হয়েছে?


# product_wise_sales = df.groupby("Product")["Sales"].sum()

# plt.bar(product_wise_sales.index,
#         product_wise_sales.values)

# plt.xlabel("Product")
# plt.ylabel("Total Sales")
# plt.title("Sales by Product")

# plt.grid(axis="y")

# plt.tight_layout()



# # #4 🌍 কোন region থেকে বেশি sales?
# region_sales = df.groupby("Region")["Sales"].sum()

# plt.bar(region_sales.index,
#         region_sales.values)


# plt.xlabel("City")
# plt.ylabel("Total Sales")
# plt.title("Total region Sales")
# plt.tight_layout()
# plt.grid(axis = "y")


# #5 📊 Sales distribution কেমন?

# plt.hist(df["Sales"],
#          bins = 5,
#          edgecolor = "black")

# plt.xlabel("Sales")
# plt.ylabel("Number of Orders")
# plt.title("Sales Distribution")

# plt.grid(axis="y")

# plt.tight_layout()



# #6 💵 Sales vs Profit-এর relationship কেমন?

# plt.scatter(df["Sales"],
#             df["Profit"],
#             s = 105,
#             alpha = 0.5)
# plt.xlabel("Sales")
# plt.ylabel("Profit")
# plt.title("Sales vs Profit")

# plt.grid()

# plt.tight_layout()



#7 🔥 কোন মাসে highest sales?

# df = pd.read_csv("Matplotlib/sales.csv")
# df["Date"] = pd.to_datetime(df["Date"])

# df["Month"] = df["Date"].dt.month_name()
# monthly_sales = df.groupby("Month")["Sales"].sum()


# fig , ax = plt.subplots(2,2 , figsize = (10,5))
# #1
# ax[0,0].plot(monthly_sales.index,
#              monthly_sales.values)

# ax[0, 0].set_title("Monthly Sales")
# ax[0, 0].set_xlabel("Month")
# ax[0, 0].set_ylabel("Sales")
# ax[0, 0].grid(axis="y")

# #2
# category_sales = df.groupby("Category")["Sales"].sum()
# ax[0,1].bar(category_sales.index,
#             category_sales.values)
 
# ax[0, 1].set_title("Sales by Category")
# ax[0, 1].set_xlabel("Category")
# ax[0, 1].set_ylabel("Sales")


# #3
# region_sales = df.groupby("Region")["Sales"].sum()
# ax[1,0].bar(region_sales.index,
#             region_sales.values,
#             color = "Blue")

# ax[1, 0].set_title("Sales by Region")
# ax[1, 0].set_xlabel("Region")
# ax[1, 0].set_ylabel("Sales")

# #4
# ax[1,1].hist(df["Sales"] ,
#              bins = 6 , 
#              color = "Red")
# ax[1, 1].set_title("Sales Distribution")
# ax[1, 1].set_xlabel("Sales")
# ax[1, 1].set_ylabel("Orders")

# plt.tight_layout()
# plt.show()



#pie chart 

category_sales = df.groupby("Category")["Sales"].sum()

plt.pie(category_sales.values,
        labels = category_sales.index,
        autopct= "%1.1f%%",
        explode=[0.1,0])
plt.title("Category Sales Share")
plt.tight_layout()
plt.savefig("Matplotlib/category_sales_share.png" , dpi = 300)
plt.show()