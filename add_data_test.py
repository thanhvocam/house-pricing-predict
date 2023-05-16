import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from functions import fill_data, replace_data, compute_corr, find_cat_variable, find_num_variable, find_num_variable2, compute_rmse, fill_test_columns, fill_train_columns, fill_test_row


train = pd.read_csv("/home/hoangthanh/Desktop/house_price_prediction/data/train.csv")
test = pd.read_csv("/home/hoangthanh/Desktop/house_price_prediction/data/test.csv")
test = fill_test_row(test)

train.drop("Id", axis = 1, inplace = True)
test.drop("Id", axis = 1, inplace = True)


# Handle missing values for features where median/mean or most common value doesn't make sense
df_train = fill_data(train)
df_train = replace_data(train)
y = df_train.SalePrice

df_test = fill_data(test)
df_test = replace_data(test)


# Find most important features relative to target
correlation = compute_corr(df_train)
print(correlation)


# Differentiate numerical features (minus the target) and categorical features
numerical_features = find_num_variable(df_train)
categorical_features = find_cat_variable(df_train)
df_train_num = df_train[numerical_features]
df_train_cat = df_train[categorical_features]
numerical_features1 = find_num_variable2(df_test)
categorical_features1 = find_cat_variable(df_test)
df_test_num = df_test[numerical_features1]
df_test_cat = df_test[categorical_features1]

# Handle remaining missing values for numerical features by using median as replacement
df_train_num = df_train_num.fillna(df_train_num.median())
df_test_num = df_test_num.fillna(df_test_num.median())


# Create dummy features for categorical values via one-hot encoding
df_train_cat = pd.get_dummies(df_train_cat)
df_test_cat = pd.get_dummies(df_test_cat)

# Fill row, columns for df_test_cat, df_train_cat
df_test_cat = fill_test_columns(df_test_cat)
df_train_cat = fill_train_columns(df_train_cat)



# Join categorical and numerical features
df_train = pd.concat([df_train_num, df_train_cat], axis = 1)
df_test = pd.concat([df_test_num, df_test_cat], axis = 1)


# Partition the dataset in train + validation sets
X_train, X_test, y_train, y_test = train_test_split(df_train, y, test_size = 0.3, random_state = 0)
print("X_train : " + str(X_train.shape))
print("X_test : " + str(X_test.shape))
print("y_train : " + str(y_train.shape))
print("y_test : " + str(y_test.shape))

X_train1, X_test1, y_train1, y_test1 = train_test_split(df_test, y, test_size = 0.3, random_state = 0)
print("X_train1 : " + str(X_train1.shape))
print("X_test1 : " + str(X_test1.shape))
print("y_train1 : " + str(y_train1.shape))
print("y_test1 : " + str(y_test1.shape))


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