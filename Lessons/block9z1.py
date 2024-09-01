def sum1(int_list):
    return sum(int_list)

def len1(int_list):
    return len(int_list)

def sorted1(int_list):
    int_list.sorted()
    return int_list

def min1(int_list):
    return min(int_list)

def max1(int_list):
    return max(int_list)

def apply_all_func(int_list, *functions):
    result={}
    for funck in functions:
        result[funck.__name__] = funck(int_list)
    return result




print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))