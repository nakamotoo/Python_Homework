#問26 LCSの全ての対応

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
    def pr(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                print(self.table[i][j]," ",end="")
            print()

    def traceback(self):
        x = ""
        y = ""
        i = len(self.x)
        j = len(self.y)
        while i>0 or j>0:
            if i>0 and j>0 and self.table[i][j] == self.table[i-1][j-1]+1 and self.x[i-1] == self.y[j-1]:
                i -= 1
                j -= 1
                x = self.x[i] + x
                y = self.y[j] + y
            elif i>0 and j>0 and self.table[i][j] == self.table[i-1][j-1] and self.x[i-1] != self.y[j-1]:
                i -= 1
                j -= 1
                x = self.x[i] + x
                y = self.y[j] + y
            elif j>0 and self.table[i][j] == self.table[i][j-1]:
                j -= 1
                x = "-" + x
                y = self.y[j] + y
            else:
                i -= 1
                x = self.x[i] + x
                y = "-" + y
        return [x,y]

def test():
    t = Lcs("abb","aab")
    tb = t.traceback()
    print(tb[0])
    print(tb[1])
test()
