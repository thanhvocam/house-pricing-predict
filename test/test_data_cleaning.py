from data_cleaning import check_category
import pandas as pd

def test_check_category():
    df_train = pd.read_csv("/home/hoangthanh/Desktop/house_price_prediction/data/train.csv")
    output = check_category(df_train)
    assert "MSZoning" in output