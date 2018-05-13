#問12 単純整列法のプログラムを動かす
import random
random.seed(100)

#単純整列法のプログラムを定義
def simplesort(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[j] < a[min]:
                min = j
        a[i],a[min] = a[min],a[i]
    return a

a = [random.random() for i in range(10000)]
b = [random.random() for i in range(1000)]

#a.sort()と一致することを確認
def test1():
    a.sort()
    return simplesort(a) == a

print(test1()) #True

#計算時間から計算量を確認
import time
def test2():
    #10000個の数字を整列する時間を求める
    t1 = time.time()
    simplesort(a)
    ta = time.time() - t1
    #1000個の数字を整列する時間を求める
    t2 = time.time()
    simplesort(b)
    tb = time.time() - t2
    print("データ数10000個の整列時間は" + str(ta))
    print("データ数1000個の整列時間は" + str(tb))
    print("両者は " + str(ta/tb) + " 違う")

test2()
print("実行結果より、データ数が10倍になると、計算時間は約100倍になるので、計算量はO(N^2)")
