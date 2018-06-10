#問41

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

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,v):
        self.stack.append(v)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

class ParsePost:
    def __init__(self,line):
        self.com = line.split(" ")
        for i in range(len(self.com)):
            if "0" <= self.com[i][0]  <= "9":
                self.com[i] = float(self.com[i])
    def e(self):
        s = Stack()
        for c in self.com:
            if c in ["+","-","*","/","^"]:
                r = s.pop()
                l = s.pop()
                s.push(ParseNodes(c,l,r))
            if c == "&":      # &の場合を追加
                
            else:
                s.push(ParseNodes(float(c)))
        return s.pop()

def test():
    i = ParsePost("1 2 + 1 & 1  @ 1 @ *")
    t = i.e()
    print(t.inorder(),"=",t.value())
test()
