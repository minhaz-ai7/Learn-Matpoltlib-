import pandas as pd 

df = pd.read_csv("house_prediction/house_pre_data.csv")

# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())


df = df.drop(columns=["Id"])

# print(df.head())
# print(df["Garage"].unique())

garage = {
    "Yes" : 1 ,
    "No" : 0
}

df["Garage"] = df["Garage"].map(garage)

# print(df["Condition"].unique())


df = pd.get_dummies(
    df,
    columns=["Location"],
    dtype=int
)

# print(df.head())


condition = {
    "Poor" : 0 ,
    "Fair" : 1 ,
    "Good" : 2 ,
    "Excellent" : 3
}

df['Condition'] = df["Condition"].map(condition)


# print(df["Condition"].value_counts())

# x = df.drop(columns=["Id" , "Price"])
# y = df["Price"]

# print(df["Condition"].unique())
# print(df["Location"].unique())
# print(df["Garage"].unique())

# print(df["Location"].value_counts())
# print(df["Condition"].value_counts())
# print(df["Garage"].value_counts())


# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())



