import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
import math

df_train = pd.read_csv("/home/hoangthanh/Desktop/house_price_prediction/data/train.csv")
# profile = ProfileReport(df_train, title="Pandas Profiling Report for house price califonia dataset")
# profile.to_file("/kaggle/working/HousePriceCalifonia_train_profiling.html")

def check_category(data):
    ls_category = []
    for i in data:
        for j in range(len(data)):
            if type(data[i][j]) is str:
                ls_category.append(i)
                break
    return ls_category
ls_category = check_category(df_train)
print(ls_category)

def check_numerical(data):
    ls_numerical = []
    for i in data:
        if i not in ls_category:
            ls_numerical.append(i)
    return ls_numerical
ls_numerical = check_numerical(df_train)
print(ls_numerical)

def check_missingvalues(data):
    ls_count = []
    for column in ls_numerical:
        missing_values = sum(data[column].isna())
        ls_count.append(missing_values)
    return ls_count 
ls_count = check_missingvalues(df_train)
print(ls_count)



