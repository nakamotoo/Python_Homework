#問17 線形探索法
import time

def find(t,s):
    for i in range(len(t)):
        if t[i] == s:
            return i
    return None

def test():
    with open("word.dat") as f:
        buf = f.readlines()
    word = [buf[i].strip() for i in range(len(buf))]
    t0 = time.time()
    index = find(word,"soccer")
    t1 = time.time() - t0
    print("soccerは"+str(index)+"番目です")
    print("所要時間は",str(t1))
test()
