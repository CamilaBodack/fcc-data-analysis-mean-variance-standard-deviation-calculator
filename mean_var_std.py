import numpy as np


def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    reshaped = np.array(list).reshape(3,3)
    mean_rows = reshaped.mean(axis=0).tolist()
    mean_cols = reshaped.mean(axis=1).tolist()
    mean_all_axis = reshaped.mean()
    variance_rows = reshaped.var(axis=0).tolist()
    variance_cols = reshaped.var(axis=1).tolist()
    variance_all_axis = reshaped.var()
    std_rows = reshaped.std(axis=0).tolist()
    std_cols = reshaped.std(axis=1).tolist()
    std_all_axis = reshaped.std()
    max_rows = reshaped.max(axis=0).tolist()
    max_cols = reshaped.max(axis=1).tolist()
    max_all_axis = reshaped.max()
    min_rows = reshaped.min(axis=0).tolist()
    min_cols = reshaped.min(axis=1).tolist()
    min_all_axis = reshaped.min()
    sum_rows = reshaped.sum(axis=0).tolist()
    sum_cols = reshaped.sum(axis=1).tolist()
    sum_all_axis = reshaped.sum()

    return {
        'mean': [mean_rows, mean_cols, mean_all_axis],
        'variance': [variance_rows, variance_cols, variance_all_axis],
        'standard deviation': [std_rows, std_cols, std_all_axis],
        'max': [max_rows, max_cols, max_all_axis],
        'min': [min_rows, min_cols, min_all_axis],
        'sum': [sum_rows, sum_cols, sum_all_axis]
        }
