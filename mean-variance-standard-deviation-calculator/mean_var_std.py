import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    arr1 = np.array(list)
    arr2 = arr1.reshape(3,3)

    mean_column = [arr2[:,0].mean(), arr2[:,1].mean(), arr2[:,2].mean()]
    mean_row = [arr2[0,:].mean(), arr2[1,:].mean(),arr2[2,:].mean()]
    mean_flat = arr1.mean()

    var_column = [arr2[:,0].var(), arr2[:,1].var(), arr2[:,2].var()]
    var_row =  [arr2[0,:].var(), arr2[1,:].var(), arr2[2,:].var()]
    var_flat = arr1.var()

    std_column = [arr2[:,0].std(), arr2[:,1].std(), arr2[:,2].std()]
    std_row = [arr2[0,:].std(), arr2[1,:].std(), arr2[2,:].std()]
    std_flat = arr1.std()

    min_column = [arr2[:,0].min(), arr2[:,1].min(), arr2[:,2].min()]
    min_row = [arr2[0,:].min(), arr2[1,:].min(), arr2[2,:].min()]
    min_flat = arr1.min()

    max_column = [arr2[:,0].max(), arr2[:,1].max(), arr2[:,2].max()]
    max_row = [arr2[0,:].max(), arr2[1,:].max(), arr2[2,:].max()]
    max_flat = arr1.max()

    sum_column = [arr2[:,0].sum(), arr2[:,1].sum(), arr2[:,2].sum()]
    sum_row= [arr2[0,:].sum(), arr2[1,:].sum(), arr2[2,:].sum()]
    sum_flat = arr1.sum()

    return {
    'mean': [mean_column, mean_row, mean_flat],
    'variance': [var_column, var_row, var_flat],
    'standard deviation': [std_column, std_row, std_flat],
    'max': [max_column, max_row, max_flat],
    'min': [min_column, min_row, min_flat],
    'sum': [sum_column, sum_row, sum_flat]
    }