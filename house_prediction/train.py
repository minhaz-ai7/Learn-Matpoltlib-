from data import df
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error , r2_score

np.random.seed(42)
df["Price"] = (
    df['Area'] * 80                          # প্রতি sqft ৮০ টাকা
    + df['Bedrooms'] * 15000                 # প্রতি bedroom ১৫,০০০
    + df['Bathrooms'] * 10000                # প্রতি bathroom ১০,০০০
    + df['Floors'] * 5000                    # প্রতি floor ৫,০০০
    - (2024 - df['YearBuilt']) * 300         # পুরনো হলে কমবে
    + df['Condition'] * 20000                # Condition ভালো হলে বাড়বে
    + df['Garage'] * 12000                   # Garage থাকলে বাড়বে
    + df['Location_Downtown'] * 50000        # Downtown হলে বাড়তি premium
    + df['Location_Suburban'] * 20000
    + np.random.normal(0, 15000, len(df))
)


x = df.drop(columns=["Price"])
y = df["Price"]


#train test split 

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)


# Feature Scaling 
std_scaler = StandardScaler()
x_train_scaler = std_scaler.fit_transform(x_train)
x_test_scaler = std_scaler.transform(x_test)
import numpy as np
# print(x_train_scaler.shape)


#model train 

model = LinearRegression()
model.fit(x_train_scaler,y_train)


#prediction 

y_pred = model.predict(x_test_scaler)

mse = mean_squared_error(y_test , y_pred)
r2_s = r2_score(y_test , y_pred)
coef = model.coef_
intercept = model.intercept_

# print(mse)
# print(r2_s)
# print(coef)
# print(intercept)

# print(df.corr()["Price"])



# print(df.corr()["Price"])


import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.scatter(y_test , y_pred , alpha=0.6 , color = "teal")
plt.plot([y_test.min() , y_test.max()] , [y_pred.min() , y_pred.max()] ,
         color ="#3e34c7",
         linewidth = 2 ,
         label = "perfect prediction")

plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted House Price')
plt.legend()

plt.savefig("house_prediction/image.png" , dpi = 120)

plt.show()


import joblib

joblib.dump(model, 'house_price_model.pkl')
joblib.dump(std_scaler, 'scaler.pkl')