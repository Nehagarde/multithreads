import sys,copy
import memory_profiler

@profile
def mem_management_for_integers():
    a = 10
    a = 2000
    b = a
    c = copy.deepcopy(a)
    d = copy.copy(a)


@profile
def mem_management_for_strings():
    a = "asdsad"
    a = "dsffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff\
        sadddasdsad10000000000000000000000ffffffffffffffffffffffffffffff"
    b = a
    c = copy.deepcopy(a)
    d = copy.copy(a)
    e = [a,c]


@profile
def mem_management_for_lists():
    a = [1,2,3]
    a = [1,2,3,1,a]
    b = a
    c = copy.deepcopy(a)
    d = copy.copy(a)

@profile
def mem_management_for_dict():
    a = {"asd":"1","dsafsf":"asds"}
    a = [1, 2, 3, 1, a]
    b = a
    c = copy.deepcopy(a)
    d = copy.copy(a)



    mem_management_for_integers()