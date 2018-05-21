#問23
import RNase_P

class Lcs:
#まずは講義資料より, LCS長のtableを求める
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

#LCS長のtableから，LCSを構成
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

def test():
    a = RNase_P.seq0()
    b = RNase_P.seq1()
    t = Lcs(a,b)
    lcs = t.print_lcs()
    #lcsを出力
    print(lcs)
    #tableの一番右下の長さを一致するか確認
    i = len(a)-1
    j = len(b)-1
    print(len(lcs) == t.table[i][j])
test()
