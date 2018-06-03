#問31 式木に冪乗演算子を追加

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
            elif self.op == "^":  # 冪乗演算子を追加
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

def test(): # 2*[(3+4)**3] の式木を作る
    x = ParseNodes("*",    # *の演算子
            ParseNodes(2), # *の左の式
            ParseNodes("^", #^の演算子
                ParseNodes("+",ParseNodes(3),ParseNodes(4)), # ^の右のしき
                ParseNodes(3) # ^の左の式
            ) # * の右の式
        )
    print(x.inorder())
    print(x.preorder())
    print(x.postorder())
    print(x.value())
    print(x.value() == 2*7**3)
test()
