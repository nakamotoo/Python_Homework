#問42 冪乗演算子の追加

class ParseNodes:
    def __init__(self,op,left=None,right=None):
        self.op = op
        self.left = left
        self.right = right
    def value(self):
        if self.left == None:
            return self.op
        else:
            l = self.left.value()
            r = self.right.value()
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
    def inorder(self):
        if self.left == None:
            return str(self.op)
        else:
            return "(" + self.left.inorder() + self.op + self.right.inorder() + ")"
    def preorder(self):
        if self.left == None:
            return str(self.op)
        else:
            return self.op + "(" + self.left.preorder() + "," + self.right.preorder() + ")"
    def postorder(self):
        if self.left == None:
            return str(self.op)
        else:
            return self.left.postorder() + " " + self.right.postorder() + self.op

class ParseExp:
    def __init__(self,line):
        self.com = line.split(" ")
        for i in range(len(self.com)):
            if "0" <= self.com[i] <= "9":
                self.com[i] = float(self.com[i])
    def t(self):
        nd = self.f()
        while len(self.com)>0 and self.com[0] in ["*","/","^"]: #"^"を追加
            op = self.com.pop(0)
            nd = ParseNodes(op,nd,self.f())
        return nd
    def e(self):
        nd = self.t()
        while len(self.com)>0 and self.com[0] in ["+","-","^"]: #"^"を追加
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
        else:
            return None

def test():
    i = ParseExp("2 * ( 3 ^ 2 + 4 )")
    n = i.e()
    print(n.inorder())
    print(n.preorder())
    print(n.postorder())
    print(n.value())
test()
