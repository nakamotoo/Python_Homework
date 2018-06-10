#問43 変数を使えるようにする

class ParseNodes:
    def __init__(self,op,left=None,right=None):
        self.op = op
        self.left = left
        self.right = right
    def value(self, bind=None):  #引数bindを追加
        if self.left == None:
            if self.op in bind.keys():    #ここを追加
                return bind[self.op]
            return self.op
        else:
            l = self.left.value(bind)
            r = self.right.value(bind)
            if self.op == "+":
                return l+r
            elif self.op == "-":
                return l-r
            elif self.op == "*":
                return l*r
            elif self.op == "/":
                return l/r
            elif self.op == "^":
                return l**r

class ParseExp:
    def __init__(self,line):
        self.com = line.split(" ")
        for i in range(len(self.com)):
            if "0" <= self.com[i] <= "9":
                self.com[i] = float(self.com[i])
    def t(self):
        nd = self.f()
        while len(self.com)>0 and self.com[0] in ["*","/","^"]:
            op = self.com.pop(0)
            nd = ParseNodes(op,nd,self.f())
        return nd
    def e(self):
        nd = self.t()
        while len(self.com)>0 and self.com[0] in ["+","-","^"]:
            op = self.com.pop(0)
            nd = ParseNodes(op,nd,self.t())
        return nd
    def f(self):
        if type(self.com[0]) == float:
            v = self.com.pop(0)
            return ParseNodes(v)
        elif self.com[0] == "(":
            self.com.pop(0)
            nd = self.e()
            self.com.pop(0)
            return nd
        elif self.com[0].islower() == True:  #先頭が英小文字の場合
            v = self.com.pop(0)
            return ParseNodes(v)      #文字列を葉にそのまま保存
        else:
            return None

def test():
    i = ParseExp("x * ( y + z )")
    n = i.e()
    print("x * ( y + z )")
    print({"x":2,"y":3,"z":4})
    print("を計算する")
    print(n.value({"x":2,"y":3,"z":4}))
test()
