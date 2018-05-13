#問20 二分探索方を改良して、指定された文字列の一個後ろの文字列を探す

#二分探索法の定義
def find(t,s):
    i = 0
    j = len(t)-1
    while i<=j:
        k = (i+j)//2
        if t[k]==s:
            if t[k+1] != None:
                return t[k+1]
            #一個後ろの文字列が存在しない場合
            else:
                return None
        elif t[k] < s:
            i = k+1
        else:
            j = k-1
    return None

def test():
    with open("word.dat") as f:
        buf = f.readlines()
    word = [buf[i].strip() for i in range(len(buf))]
    w = find(word, "soccer")
    print("soccerの次の単語は:",w)

test()
