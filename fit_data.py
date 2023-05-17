# Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from functions import fill_data, replace_data, compute_corr, find_cat_variable, find_num_variable, compute_rmse
import matplotlib.pyplot as plt



train = pd.read_csv("/home/hoangthanh/Desktop/house_price_prediction/data/train.csv")
train = train[train.GrLivArea < 4000]
train.drop("Id", axis = 1, inplace = True)

# Handle missing values for features where median/mean or most common value doesn't make sense
df_train = fill_data(train)
df_train = replace_data(train)
y = df_train.SalePrice

# Find most important features relative to target
correlation = compute_corr(df_train)

# Differentiate numerical features (minus the target) and categorical features
numerical_features = find_num_variable(df_train)
categorical_features = find_cat_variable(df_train)
numerical_features = numerical_features.drop("SalePrice")
df_train_num = df_train[numerical_features]
df_train_cat = df_train[categorical_features]

# Handle remaining missing values for numerical features by using median as replacement
df_train_num = df_train_num.fillna(df_train_num.median())

# Create dummy features for categorical values via one-hot encoding
df_train_cat = pd.get_dummies(df_train_cat)

# Join categorical and numerical features
df_train = pd.concat([df_train_num, df_train_cat], axis = 1)

# Partition the dataset in train + validation sets
X_train, X_test, y_train, y_test = train_test_split(df_train, y, test_size = 0.3, random_state = 0)
print("X_train : " + str(X_train.shape))
print("X_test : " + str(X_test.shape))
print("y_train : " + str(y_train.shape))
print("y_test : " + str(y_test.shape))



# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

# Define error measure for official scoring : RMSE
y_train_pred = lr.predict(X_train)
y_test_pred = lr.predict(X_test)


rmse_train_model = compute_rmse(y_train_pred,y_train)
print("rmse_train_model_value:", rmse_train_model)
rmse_test_model = compute_rmse(y_test_pred, y_test)
print("rmse_test_model_value:", rmse_test_model)


# Plot predictions
plt.scatter(y_train_pred, y_train, c = "blue", marker = "s", label = "Training data")
plt.scatter(y_test_pred, y_test, c = "lightgreen", marker = "s", label = "Validation data")
plt.title("Linear regression")
plt.xlabel("Predicted values")
plt.ylabel("Real values")
plt.legend(loc = "upper left")
plt.plot([0, 600000], [0, 600000], c = "red")
plt.show()

# Plot residuals
plt.scatter(y_train_pred, y_train_pred - y_train, c = "blue", marker = "s", label = "Training data")
plt.scatter(y_test_pred, y_test_pred - y_test, c = "lightgreen", marker = "s", label = "Validation data")
plt.title("Linear regression")
plt.xlabel("Predicted values")
plt.ylabel("Residuals")
plt.legend(loc = "upper left")
plt.hlines(y = 0, xmin = 0, xmax = 600000, color = "red")
plt.show()