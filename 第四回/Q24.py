#問24 edit距離

#まずはlcsを求める
class Lcs:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.table = [[0 for j in range(len(self.y)+1)] for i in range(len(self.x)+1)]
        for i in range(1,len(self.x)+1):
            for j in range(1,len(self.y)+1):
                if self.x[i-1] == self.y[j-1]:
                    self.table[i][j] = self.table[i-1][j-1]+1
                elif self.table[i-1][j] > self.table[i][j-1]:
                    self.table[i][j] = self.table[i-1][j]
                else:
                    self.table[i][j] = self.table[i][j-1]

    def print_lcs(self):
        lcs = ""
        i = len(self.x)
        j = len(self.y)
        while i>0 or j>0:
            if i>0 and j>0 and self.table[i][j] == self.table[i-1][j-1]+1 and self.x[i-1] == self.y[j-1]:
                i -= 1
                j -= 1
                lcs = self.x[i] + lcs
            elif i>0 and j>0 and self.table[i][j] == self.table[i-1][j-1] and self.x[i-1] != self.y[j-1]:
                i -= 1
                j -= 1
            elif j>0 and self.table[i][j] == self.table[i][j-1]:
                j -= 1
            else:
                i -= 1
        return lcs

#次に，edit距離を考える
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
    # print m
    return m

#上の表から，どのような操作が行われたかをバックトレースする
#引数: editDistance()の出力m
def traceback(tgt,inp):
    m = editDistance(tgt,inp)
    step = []
    i = len(m)-1
    j = len(m[0])-1
    while i>0 or j>0:
        # 挿入（insert）の場合:
        if i>0 and j>0 and m[i][j] == m[i - 1][j] + 1:
            i -= 1
            step = ["i"] + step
        # 削除 (delete) の場合:
        elif i>0 and j>0 and m[i][j] == m[i][ j - 1] + 1:
            j -= 1
            step = ["d"] + step
        #置換 (change) の場合:
        elif i>0 and j>0 and m[i][j] == m[i - 1][ j - 1] + 1:
            j -= 1
            i -= 1
            step = ["c"] + step
        elif i>0 and j>0 and m[i][j] == m[i - 1][ j - 1]:
            j -= 1
            i -= 1
    return step


def test():
    a = "私たちは東京大学の学生です"
    b = "私達は東大の学生です!"
    t = Lcs(a,b)
    lcs = t.print_lcs()
    print("目標:",a)
    print("入力:",b)
    print("LCS:",lcs)
    m = editDistance(a,b)
    print("編集距離:",m[-1][-1])
    step = traceback(a,b)
    print("行った操作 i(nsert)/d(elete)/c(hange):",step)
    print("iが多かったので，文字を多く抜かしてしまう癖がある．")

test()
