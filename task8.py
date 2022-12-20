def get_number_from_Fibanocci_series(max):

    if max == 0:
        return 0
    
    if max == 1 or max == 2:
        return 1
    
    else:
        result = get_number_from_Fibanocci_series(max - 2) + get_number_from_Fibanocci_series(max - 1)
        return result
    
print(get_number_from_Fibanocci_series(10))