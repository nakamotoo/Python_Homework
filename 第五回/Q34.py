#問34 replaceConstant()メソッドを追加

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

    #ここメソッドをに追加
    def replaceConstant(self, c1, c2):
        if self.left == None:
            if self.op == c1:
                self.op = c2
        else:
            self.left.replaceConstant(c1, c2)
            self.right.replaceConstant(c1, c2)

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

def test():
    x = ParseNodes("*",
        ParseNodes(2),
        ParseNodes("+",ParseNodes(3),ParseNodes(2))
        )
    print('元のinorder: ',x.inorder())
    print('元のvalue: ',x.value())
    print("2を5に置き換える")
    x.replaceConstant(2,5)
    print('処理後のinorder: ',x.inorder())
    print('処理後のvalue: ',x.value())
test()
