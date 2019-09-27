import sys,copy
import memory_profiler

@profile
def function():
    x = list(range(1000000))  # allocate a big list
    y = copy.deepcopy(x)
    del x
    return y


@profile
def mem_management_for_integers():
    a = 10


if __name__ == '__main__':
    function()
    mem_management_for_integers()
