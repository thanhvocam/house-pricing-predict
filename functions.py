import math

def fill_data(data):
    data.loc[:, "Alley"] = data.loc[:, "Alley"].fillna("None")
    data.loc[:, "BedroomAbvGr"] = data.loc[:, "BedroomAbvGr"].fillna(0)
    data.loc[:, "BsmtQual"] = data.loc[:, "BsmtQual"].fillna("No")
    data.loc[:, "BsmtCond"] = data.loc[:, "BsmtCond"].fillna("No")
    data.loc[:, "BsmtExposure"] = data.loc[:, "BsmtExposure"].fillna("No")
    data.loc[:, "BsmtFinType1"] = data.loc[:, "BsmtFinType1"].fillna("No")
    data.loc[:, "BsmtFinType2"] = data.loc[:, "BsmtFinType2"].fillna("No")
    data.loc[:, "BsmtFullBath"] = data.loc[:, "BsmtFullBath"].fillna(0)
    data.loc[:, "BsmtHalfBath"] = data.loc[:, "BsmtHalfBath"].fillna(0)
    data.loc[:, "BsmtUnfSF"] = data.loc[:, "BsmtUnfSF"].fillna(0)
    data.loc[:, "CentralAir"] = data.loc[:, "CentralAir"].fillna("N")
    data.loc[:, "Condition1"] = data.loc[:, "Condition1"].fillna("Norm")
    data.loc[:, "Condition2"] = data.loc[:, "Condition2"].fillna("Norm")
    data.loc[:, "EnclosedPorch"] = data.loc[:, "EnclosedPorch"].fillna(0)
    data.loc[:, "ExterCond"] = data.loc[:, "ExterCond"].fillna("TA")
    data.loc[:, "ExterQual"] = data.loc[:, "ExterQual"].fillna("TA")
    data.loc[:, "Fence"] = data.loc[:, "Fence"].fillna("No")
    data.loc[:, "FireplaceQu"] = data.loc[:, "FireplaceQu"].fillna("No")
    data.loc[:, "Fireplaces"] = data.loc[:, "Fireplaces"].fillna(0)
    data.loc[:, "Functional"] = data.loc[:, "Functional"].fillna("Typ")
    data.loc[:, "GarageType"] = data.loc[:, "GarageType"].fillna("No")
    data.loc[:, "GarageFinish"] = data.loc[:, "GarageFinish"].fillna("No")
    data.loc[:, "GarageQual"] = data.loc[:, "GarageQual"].fillna("No")
    data.loc[:, "GarageCond"] = data.loc[:, "GarageCond"].fillna("No")
    data.loc[:, "GarageArea"] = data.loc[:, "GarageArea"].fillna(0)
    data.loc[:, "GarageCars"] = data.loc[:, "GarageCars"].fillna(0)
    data.loc[:, "HalfBath"] = data.loc[:, "HalfBath"].fillna(0)
    data.loc[:, "HeatingQC"] = data.loc[:, "HeatingQC"].fillna("TA")
    data.loc[:, "KitchenAbvGr"] = data.loc[:, "KitchenAbvGr"].fillna(0)
    data.loc[:, "KitchenQual"] = data.loc[:, "KitchenQual"].fillna("TA")
    data.loc[:, "LotFrontage"] = data.loc[:, "LotFrontage"].fillna(0)
    data.loc[:, "LotShape"] = data.loc[:, "LotShape"].fillna("Reg")
    data.loc[:, "MasVnrType"] = data.loc[:, "MasVnrType"].fillna("None")
    data.loc[:, "MasVnrArea"] = data.loc[:, "MasVnrArea"].fillna(0)
    data.loc[:, "MiscFeature"] = data.loc[:, "MiscFeature"].fillna("No")
    data.loc[:, "MiscVal"] = data.loc[:, "MiscVal"].fillna(0)
    data.loc[:, "OpenPorchSF"] = data.loc[:, "OpenPorchSF"].fillna(0)
    data.loc[:, "PavedDrive"] = data.loc[:, "PavedDrive"].fillna("N")
    data.loc[:, "PoolQC"] = data.loc[:, "PoolQC"].fillna("No")
    data.loc[:, "PoolArea"] = data.loc[:, "PoolArea"].fillna(0)
    data.loc[:, "SaleCondition"] = data.loc[:, "SaleCondition"].fillna("Normal")
    data.loc[:, "ScreenPorch"] = data.loc[:, "ScreenPorch"].fillna(0)
    data.loc[:, "TotRmsAbvGrd"] = data.loc[:, "TotRmsAbvGrd"].fillna(0)
    data.loc[:, "Utilities"] = data.loc[:, "Utilities"].fillna("AllPub")
    data.loc[:, "WoodDeckSF"] = data.loc[:, "WoodDeckSF"].fillna(0)
    return data

def replace_data(data):
    data = data.replace({"MSSubClass" : {20 : "SC20", 30 : "SC30", 40 : "SC40", 45 : "SC45", 
                                        50 : "SC50", 60 : "SC60", 70 : "SC70", 75 : "SC75", 
                                        80 : "SC80", 85 : "SC85", 90 : "SC90", 120 : "SC120", 
                                        150 : "SC150", 160 : "SC160", 180 : "SC180", 190 : "SC190"},
                        "MoSold" : {1 : "Jan", 2 : "Feb", 3 : "Mar", 4 : "Apr", 5 : "May", 6 : "Jun",
                                    7 : "Jul", 8 : "Aug", 9 : "Sep", 10 : "Oct", 11 : "Nov", 12 : "Dec"}
                        })
    data = data.replace({"Alley" : {"Grvl" : 1, "Pave" : 2},
                        "BsmtCond" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "BsmtExposure" : {"No" : 0, "Mn" : 1, "Av": 2, "Gd" : 3},
                        "BsmtFinType1" : {"No" : 0, "Unf" : 1, "LwQ": 2, "Rec" : 3, "BLQ" : 4, 
                                            "ALQ" : 5, "GLQ" : 6},
                        "BsmtFinType2" : {"No" : 0, "Unf" : 1, "LwQ": 2, "Rec" : 3, "BLQ" : 4, 
                                            "ALQ" : 5, "GLQ" : 6},
                        "BsmtQual" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA": 3, "Gd" : 4, "Ex" : 5},
                        "ExterCond" : {"Po" : 1, "Fa" : 2, "TA": 3, "Gd": 4, "Ex" : 5},
                        "ExterQual" : {"Po" : 1, "Fa" : 2, "TA": 3, "Gd": 4, "Ex" : 5},
                        "FireplaceQu" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "Functional" : {"Sal" : 1, "Sev" : 2, "Maj2" : 3, "Maj1" : 4, "Mod": 5, 
                                        "Min2" : 6, "Min1" : 7, "Typ" : 8},
                        "GarageCond" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "GarageQual" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "HeatingQC" : {"Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "KitchenQual" : {"Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                        "LandSlope" : {"Sev" : 1, "Mod" : 2, "Gtl" : 3},
                        "LotShape" : {"IR3" : 1, "IR2" : 2, "IR1" : 3, "Reg" : 4},
                        "PavedDrive" : {"N" : 0, "P" : 1, "Y" : 2},
                        "PoolQC" : {"No" : 0, "Fa" : 1, "TA" : 2, "Gd" : 3, "Ex" : 4},
                        "Street" : {"Grvl" : 1, "Pave" : 2},
                        "Utilities" : {"ELO" : 1, "NoSeWa" : 2, "NoSewr" : 3, "AllPub" : 4}}
                        )
    data["SimplOverallQual"] = data.OverallQual.replace({1 : 1, 2 : 1, 3 : 1, # bad
                                                        4 : 2, 5 : 2, 6 : 2, # average
                                                        7 : 3, 8 : 3, 9 : 3, 10 : 3 # good
                                                        })
    data["SimplOverallCond"] = data.OverallCond.replace({1 : 1, 2 : 1, 3 : 1, # bad
                                                        4 : 2, 5 : 2, 6 : 2, # average
                                                        7 : 3, 8 : 3, 9 : 3, 10 : 3 # good
                                                        })
    data["SimplPoolQC"] = data.PoolQC.replace({1 : 1, 2 : 1, # average
                                                3 : 2, 4 : 2 # good
                                                })
    data["SimplGarageCond"] = data.GarageCond.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    data["SimplGarageQual"] = data.GarageQual.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    data["SimplFireplaceQu"] = data.FireplaceQu.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    data["SimplFireplaceQu"] = data.FireplaceQu.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    data["SimplFunctional"] = data.Functional.replace({1 : 1, 2 : 1, # bad
                                                        3 : 2, 4 : 2, # major
                                                        5 : 3, 6 : 3, 7 : 3, # minor
                                                        8 : 4 # typical
                                                        })
    data["SimplKitchenQual"] = data.KitchenQual.replace({1 : 1, # bad
                                                        2 : 1, 3 : 1, # average
                                                        4 : 2, 5 : 2 # good
                                                        })
    data["SimplHeatingQC"] = data.HeatingQC.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    data["SimplBsmtFinType1"] = data.BsmtFinType1.replace({1 : 1, # unfinished
                                                            2 : 1, 3 : 1, # rec room
                                                            4 : 2, 5 : 2, 6 : 2 # living quarters
                                                            })
    data["SimplBsmtFinType2"] = data.BsmtFinType2.replace({1 : 1, # unfinished
                                                            2 : 1, 3 : 1, # rec room
                                                            4 : 2, 5 : 2, 6 : 2 # living quarters
                                                            })
    data["SimplBsmtCond"] = data.BsmtCond.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    data["SimplBsmtQual"] = data.BsmtQual.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    data["SimplExterCond"] = data.ExterCond.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    data["SimplExterQual"] = data.ExterQual.replace({1 : 1, # bad
                                                    2 : 1, 3 : 1, # average
                                                    4 : 2, 5 : 2 # good
                                                    })
    # Has masonry veneer or not 
    data["HasMasVnr"] = data.MasVnrType.replace({"BrkCmn" : 1, "BrkFace" : 1, "CBlock" : 1, 
                                                "Stone" : 1, "None" : 0})
    # House completed before sale or not
    data["BoughtOffPlan"] = data.SaleCondition.replace({"Abnorml" : 0, "Alloca" : 0, "AdjLand" : 0, 
                                                        "Family" : 0, "Normal" : 0, "Partial" : 1})
    return data

def find_cat_variable(data):
    categorical_features = data.select_dtypes(include = ["object"]).columns
    return categorical_features

def find_num_variable(data):
    numerical_features = data.select_dtypes(exclude = ["object"]).columns
    return numerical_features

def compute_corr(data):
    corr = data.corr()
    corr.sort_values(["SalePrice"], ascending = False, inplace = True)
    return corr.SalePrice

def compute_rmse(y_pred,y):
    rmse = math.sqrt(sum((y_pred - y)**2)/len(y))
    return rmse

def fill_test_columns(data):
    new_data = [0] * 1459
    for i in range(len(new_data)):
        data.loc[i, 'Condition2_RRAe'] = new_data[i]
        data.loc[i, 'Condition2_RRAn'] = new_data[i]
        data.loc[i, 'Condition2_RRNn'] = new_data[i]
        data.loc[i, 'HouseStyle_2.5Fin'] = new_data[i]
        data.loc[i, 'RoofMatl_ClyTile'] = new_data[i]
        data.loc[i, 'RoofMatl_Membran'] = new_data[i]
        data.loc[i, 'RoofMatl_Metal'] = new_data[i]
        data.loc[i, 'RoofMatl_Roll'] = new_data[i]
        data.loc[i, 'Exterior1st_ImStucc'] = new_data[i]
        data.loc[i, 'Exterior1st_Stone'] = new_data[i]
        data.loc[i, 'Exterior2nd_Other'] = new_data[i]
        data.loc[i, 'Heating_Floor'] = new_data[i]
        data.loc[i, 'Heating_OthW'] = new_data[i]
        data.loc[i, 'Electrical_Mix'] = new_data[i]
        data.loc[i, 'MiscFeature_TenC'] = new_data[i]
    return data

def fill_train_columns(data):
    new_data = [0] * 1460
    for i in range(len(new_data)):
        data.loc[i, 'MSSubClass_SC150'] = new_data[i]
    return data




        

    

      
 

