#問18 二分探索法、線形探索法、indexを使った探索の比較
import time

#線形探索法の定義
def find(t,s):
    for i in range(len(t)):
        if t[i] == s:
            return i
    return None

#二分探索法の定義
def find2(t,s):
    i = 0
    j = len(t)-1
    while i<=j:
        k = (i+j)//2
        if t[k]==s:
            return k
        elif t[k] < s:
            i = k+1
        else:
            j = k-1
    return None

#indexを使った探索の定義
def find3(t,s):
    return t.index(s)

#探索時間の比較
def test():
    with open("word.dat") as f:
        buf = f.readlines()
    word = [buf[i].strip() for i in range(len(buf))]
    #"soccer"を100回探す時間を計測
    t1 = time.time()
    for i in range(100):
        find(word,"soccer")
    time_1 = time.time() - t1
    t2 = time.time()
    for i in range(100):
        find2(word,"soccer")
    time_2 = time.time() - t2
    t3 = time.time()
    for i in range(100):
        find3(word,"soccer")
    time_3= time.time() - t3
    print("線形探索法:",str(time_1))
    print("二分探索法:",str(time_2))
    print("indexを用いた探索:",str(time_3))

test()
print("二分探索法が圧倒的に速いことがわかる")
