import sys,copy
import pandas as pd
def our_decorator(func):
    def function_wrapper():
        column_names = ['Object', 'Address', 'Memory']
        print("=================================================================")
        res = func()
        df = pd.DataFrame(res, columns=column_names)
        print(df)
        print("=================================================================")
    return function_wrapper

@our_decorator
def mem_manage_ints():
    a = 10
    data = []
    data.append(['a', id(a), sys.getsizeof(a)])

    b = 20
    data.append(['b', id(b), sys.getsizeof(b)])

    c = a
    data.append(['c', id(c), sys.getsizeof(b)])
    return data

@our_decorator
def mem_manage_lists():
    data1 = []
    l1 = [1, 2, 3, 1]
    data1.append(['l1', id(l1), sys.getsizeof(l1)])
    l2 = [1, 2, 3, 4, l1]
    data1.append(['l2', id(l2), sys.getsizeof(l2)])
    l3 = l1
    data1.append(['l3', id(l3), sys.getsizeof(l3)])
    l4 = l3
    data1.append(['l4', id(l4), sys.getsizeof(l4)])
    del l1
    data1.append(['l2', id(l2), sys.getsizeof(l2)])
    data1.append(['l3', id(l3), sys.getsizeof(l3)])
    data1.append(['l4', id(l4), sys.getsizeof(l4)])
    del l2[4]
    l5 = copy.deepcopy(l3)
    data1.append(['l5', id(l5), sys.getsizeof(l5)])
    l6 = copy.copy(l5)
    data1.append(['l6', id(l6), sys.getsizeof(l6)])
    return data1


mem_manage_ints()
mem_manage_lists()
# diff(10)