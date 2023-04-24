import pandas as pd
from data_cleaning import check_category
from data_cleaning import check_numerical
from data_cleaning import check_missingvalues

df_train = pd.read_csv("/home/hoangthanh/Desktop/house_price_prediction/data/train.csv")

def test_check_category():
    output = check_category(df_train)
    assert "MSZoning" in output

def test_check_numerical():
    output = check_numerical(df_train)
    assert "FullBath" in output

def test_check_missingvalues():
    output = check_missingvalues(df_train)
    assert isinstance(output, list)
    assert all(isinstance(i, int) for i in output)
    
    

