# Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from functions import handle_data, compute_corr, find_cat_variable, find_num_variable, compute_rmse
import matplotlib.pyplot as plt



train = pd.read_csv("/home/hoangthanh/Desktop/house_price_prediction/data/test.csv")
train.drop("Id", axis = 1, inplace = True)

# Handle missing values for features where median/mean or most common value doesn't make sense
df_train = handle_data(train)

# Find most important features relative to target
# correlation = compute_corr(df_train)

# Differentiate numerical features (minus the target) and categorical features
numerical_features = find_num_variable(df_train)
categorical_features = find_cat_variable(df_train)
df_train_num = df_train[numerical_features]
df_train_cat = df_train[categorical_features]

# Handle remaining missing values for numerical features by using median as replacement
df_train_num = df_train_num.fillna(df_train_num.median())

# Create dummy features for categorical values via one-hot encoding
df_train_cat = pd.get_dummies(df_train_cat)

# Join categorical and numerical features
df_train = pd.concat([df_train_num, df_train_cat], axis = 1)

# Partition the dataset in train + validation sets
X_train, y_train = train_test_split(df_train, test_size = 0.3, random_state = 0)
print("X_train : " + str(X_train.shape))
print("y_train : " + str(y_train.shape))



# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

# Define error measure for official scoring : RMSE
y_train_pred = lr.predict(X_train)


# rmse_train_model = compute_rmse(y_train_pred,y_train)
# print("rmse_train_model_value:", rmse_train_model)
# rmse_test_model = compute_rmse(y_test_pred, y_test)
# print("rmse_test_model_value:", rmse_test_model)

