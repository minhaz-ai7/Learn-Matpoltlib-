# House Price Prediction — Multiple Linear Regression

A Machine Learning project that predicts house prices based on features
like area, bedrooms, bathrooms, floors, year built, condition, garage,
and location — using Multiple Linear Regression.

## Problem Statement
Predict house price using multiple property features via Multiple Linear Regression.

## Dataset
- Source: Kaggle
- 2000 rows, 10 original columns
- Note: Original `Price` column had no real correlation with features
  (verified via correlation check), so a realistic price formula was
  applied to simulate a meaningful relationship for learning purposes.

## Features Used
- Numeric: Area, Bedrooms, Bathrooms, Floors, YearBuilt
- Encoded: Condition (Ordinal: Poor=0 → Excellent=3), Garage (Binary),
  Location (One-Hot Encoded: Downtown, Suburban, Rural, Urban)

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Joblib



## How to Run
\`\`\`bash
pip install -r requirements.txt
python data.py      # data loading, encoding, price formula
python train.py     # training, evaluation, visualization
\`\`\`

## Approach
1. Loaded & explored dataset (checked shape, dtypes, missing values)
2. Encoded categorical features (One-Hot for Location, Ordinal for Condition, Binary for Garage)
3. Verified feature-target correlation (found original Price uncorrelated; applied custom formula)
4. Feature Scaling (StandardScaler)
5. Train/Test Split (80/20)
6. Trained Linear Regression model
7. Evaluated with MSE and R²



![Actual vs Predicted]("house_prediction/image.png")

