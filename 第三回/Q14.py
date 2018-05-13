#問14 単純整列法と併合整列法の比較
import copy
import time
#単純整列法のプログラムを定義
def simplesort(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[j] < a[min]:
                min = j
        a[i],a[min] = a[min],a[i]
    return a

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

#pg10配列を作る
with open("pg10.dat") as f: buf = f.readlines()
pg10 = [buf[i].strip() for i in range(len(buf))]

#単純整列法と併合整列法とsort()の比較
def test1():
    #時間がかかるのでサイズを10000にしました
    list1 = copy.copy(pg10[:10000])
    list2 = copy.copy(pg10[:10000])
    list3 = copy.copy(pg10[:10000])
    t1 = time.time()
    simplesort(list1)
    time_simple0 = time.time() - t1
    t2 = time.time()
    mergesort(list2)
    time_merge0 = time.time() - t2
    t3 = time.time()
    list3.sort()
    time_sort0 = time.time() - t3

    #サイズを1/10に変更してみる
    list4 = copy.copy(pg10[:1000])
    list5 = copy.copy(pg10[:1000])
    list6 = copy.copy(pg10[:1000])
    t4 = time.time()
    simplesort(list4)
    time_simple1 = time.time() - t4
    t5 = time.time()
    mergesort(list5)
    time_merge1 = time.time() - t5
    t6 = time.time()
    list6.sort()
    time_sort1 = time.time() - t6

    print("サイズが10000の時")
    print("単純整列法:", str(time_simple0),"併合整列法:", str(time_merge0),"sort():", str(time_sort0))
    print("サイズが1000の時")
    print("単純整列法:", str(time_simple1),"併合整列法:", str(time_merge1),"sort():", str(time_sort1))
    print("(10000にかかる時間/1000にかかる時間)は:")
    print("単純整列法:", str(time_simple0/time_simple1),"併合整列法:", str(time_merge0/time_merge1),"sort():", str(time_sort0/time_sort1))
    print("これはそれぞれの計算量 O(N^2), O(Nlog_2(N), O(NlogN)に適している)")

test1()
