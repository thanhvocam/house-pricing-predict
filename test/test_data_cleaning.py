import pandas as pd
import math
from data_cleaning import check_category
from data_cleaning import check_numerical
from data_cleaning import check_missingvalues
from data_cleaning import del_na
from data_cleaning import fill_na
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

def test_del_na():
    output = del_na(df_train,"MasVnrArea")
    for i in output:
        assert math.isnan(i) is False

def test_fill_na():
    output = fill_na(df_train,"MasVnrArea",20)
    for i in output:
        assert math.isnan(i) is False


