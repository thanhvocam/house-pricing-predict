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
print(check_category(df_train))



