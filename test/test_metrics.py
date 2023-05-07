
import numpy as np
from fit_data import compute_rmse
from math import sqrt

def test_rmse_train():
    y_pred = np.array([1,2,3,4,5,6,7,8,9,10])
    y = np.array([1,2,3,4,5,6,7,8,9,11])
    rmse = compute_rmse(y, y_pred)
    assert rmse == sqrt(0.1)

    y_pred = np.array([1,2])
    y = np.array([3, 4])
    rmse = compute_rmse(y, y_pred)
    assert rmse == sqrt(4)
