#問37 二つの式木が等しいか判別する

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

#このメソッドを追加，同じ式木ならばpreorderが同じになる
def eql(a, b):
    if a.preorder() == b.preorder():
        print("同じ")
    else:
        print("異なる")

def test():
    #xとyは同じ式木，zはxの+を-にした
    x = ParseNodes("*",
        ParseNodes(2),
        ParseNodes("+",ParseNodes(3),ParseNodes(2))
        )
    y = ParseNodes("*",
        ParseNodes(2),
        ParseNodes("+",ParseNodes(3),ParseNodes(2))
        )
    z = ParseNodes("*",
        ParseNodes(2),
        ParseNodes("-",ParseNodes(3),ParseNodes(2))
        )
    eql(x, y)
    eql(x,z)
test()
