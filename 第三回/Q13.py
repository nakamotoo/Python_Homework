#問13 併合整列法のプログラムを動かす
import random
import math
random.seed(100)

#併合整列法のプログラムを定義
def mergesort(a):
    return mergesortSub(a,0,len(a))
def mergesortSub(a,l,r):
    if r > l+1:
        m = (l+r)//2
        mergesortSub(a,l,m)
        mergesortSub(a,m,r)
        merge2(a,l,m,r)
    return a
def merge2(a,l,m,r):
    c = [0 for i in range(r-l)]
    ia = l
    ib = m
    for i in range(len(c)):
        if ia >= m:
            c[i] = a[ib]
            ib = ib+1
        elif ib >= r:
            c[i] = a[ia]
            ia = ia+1
        elif a[ia] < a[ib]:
            c[i] = a[ia]
            ia = ia+1
        else:
            c[i] = a[ib]
            ib = ib+1
    for i in range(len(c)):
        a[l+i]=c[i]

a = [random.random() for i in range(100000)]
b = [random.random() for i in range(10000)]

#a.sort()と一致することを確認
def test1():
    a.sort()
    return mergesort(a) == a

print(test1()) #True

#計算時間から計算量を確認
import time
def test2():
    #32000個の数字を整列する時間を求める
    t1 = time.time()
    mergesort(a)
    ta = time.time() - t1
    #1000個の数字を整列する時間を求める
    t2 = time.time()
    mergesort(b)
    tb = time.time() - t2
    print("データ数100000個の整列時間は" + str(ta))
    print("データ数10000個の整列時間は" + str(tb))
    print("両者は " + str(ta/tb) + " 違う")

test2()
print("計算上の答えは" + str(10 * math.log(100000, 2)/math.log(10000, 2)))
print("上の数値はほぼ一致するので、計算量はO(Nlog_2(N))")
