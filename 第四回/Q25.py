#問25
# Mr.Childrenのヒットソング"innocent world"の一番のサビと最後のサビを比べてみる

def editDistance(tgt,inp):
    m = [ [0] * (len(inp) + 1) for i in range(len(tgt) + 1) ]

    #表の1列目は0,1,2,3...
    for i in range(len(tgt) + 1):
        m[i][0] = i

    #表の1行目も0,1,2,3...
    for j in range(len(inp) + 1):
        m[0][j] = j

    for i in range(1, len(tgt) + 1):
        for j in range(1, len(inp) + 1):
            #同じ文字は操作を加えなくて良いので x = 0
            if tgt[i - 1] == inp[j - 1]:
                x = 0
            #同じ文字ではないなら，置換するので x = 1
            else:
                x = 1
            #上，左，左上の一番小さい数字に，新たな操作の回数（0 or 1）を加える
            m[i][j] = min(m[i - 1][j] + 1, m[i][ j - 1] + 1, m[i - 1][j - 1] + x)
    return m

def cmpFile(f1,f2):
    m = editDistance(f1,f2)
    step = []
    script = []
    i = len(m)-1
    j = len(m[0])-1
    while i>0 or j>0:
        # 挿入（insert）の場合:
        if i>0 and j>0 and m[i][j] == m[i - 1][j] + 1:
            i -= 1
            step = ["i"] + step
            script = ["insert: " + f1[i]] + script
        # 削除 (delete) の場合:
        elif i>0 and j>0 and m[i][j] == m[i][ j - 1] + 1:
            j -= 1
            step = ["d"] + step
            script = ["delete: " + f2[j]] + script
        #置換 (change) の場合:
        elif i>0 and j>0 and m[i][j] == m[i - 1][ j - 1] + 1:
            j -= 1
            i -= 1
            step = ["c"] + step
            script = ["change: " + f2[j] + " -> " + f1[i]] + script
        elif i>0 and j>0 and m[i][j] == m[i - 1][ j - 1]:
            j -= 1
            i -= 1
    return step, script


def readLine(fn):
    with open(fn) as f: # ファイルを開いて読む準備をする。
        buf = f.readlines() # ファイル全体を読み込み、行を要素とする配列にする。
    lines = [buf[i].strip() for i in range(len(buf))] # 行末の改行文字を除く。
    return lines

def test():
    f1 = readLine("mrchildren0.dat")
    f2 = readLine("mrchildren1.dat")
    print("f1")
    print(f1)
    print("f2")
    print(f2)
    print()
    print("f2をどのように編集したらf1になるか知りたい")
    print()
    m = editDistance(f1,f2)
    step, script = cmpFile(f1,f2)
    print(step)
    print(script)
test()
