#問１ コム整列
import random
import copy
def comsort(a):
    h = len(a)
    swapped = False
    while h > 1 or swapped == True:
        if h > 1:
            h = (10*h)//13
        swapped = False
        for i in range(len(a)-h):
            if a[i] > a[i+h]:
                a[i], a[i+h] = a[i+h], a[i]
                swapped = True
    return a

a = [random.random() for i in range(10000)] #random.random()は0-1の乱数を生成
b = copy.copy(a)
comsort(a)
b.sort()
print(a == b)
