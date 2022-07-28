# import sys

# sys.path.append("..")
# from useful_func import *


def mergeLists(a, b):
    result = []
    if len(a) == 0 or len(b) == 0:
        if len(a) == 0 and len(b) == 0:
            return result
        elif len(a) != 0 and len(b) == 0:
            return result + a
        elif len(a) == 0 and len(b) != 0:
            return result + b
    else:
        if a[0] <= b[0]:
            result.append(a[0])
            result = result + mergeLists(a[1:], b)
        if a[0] > b[0]:
            result.append(b[0])
            result = result +  mergeLists(a, b[1:])
    return result


def mergeLists(a, b):
    result = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))

    return result + a + b

a = [1, 3, 5, 7]
b = [2, 4, 6]
print(mergeLists(a, b))


def combine(a:list, b:list):    
    alist = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            alist.append(a[i])
            i+=1
        else:
            alist.append(b[j])
            j+=1

    while i < len(a):
        alist.append(a[i])
        i+=1

    while j < len(b):
        alist.append(b[j])
        j+=1

    return alist