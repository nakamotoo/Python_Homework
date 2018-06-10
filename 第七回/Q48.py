# 問48 指定された値以下で最大のキーを探す
# 前の問題の不等号を少し変えれば良い

class Bintree:
    def __init__(self,key=None,data=None): # デフォルト値を使うのはrootのみ
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def search(self,key):
        if self.key == None:
            return None
        if key < self.key:
            if self.left == None:
                return None  # 左の子がなければない
            else:
                return self.left.search(key) # 左の子があれば左の子(の下を)再帰的に検索
        elif key >= self.key:
            if self.right == None:
                return self.key  #右の子がなければそのkeyが最大
            elif key >= self.right.key:
                return self.right.search(key)
            else:
                return self.key

    def insert(self,key,data):
        if self.key == None:
            self.key = key
            self.data = data
            return self
        if key < self.key:
            if self.left == None:
                self.left = Bintree(key,data) # 左の子がなければ、そこに頂点を作って登録
                return True
            else:
                return self.left.insert(key,data)
        elif key > self.key:
            if self.right == None:
                self.right = Bintree(key,data)
                return True
            else:
                return self.right.insert(key,data)
        else: # key == self.key:
            return False
    def to_s(self):
        return "key="+str(self.key)+" data="+str(self.data)
    def prints(self,d=0):
        if self.left != None:
            self.left.prints(d+1)
        print("  "*d,self.to_s())
        if self.right != None:
            self.right.prints(d+1)

def test1():
    root = Bintree()
    print("1. 下のような順番でinsertした時，以下のような入力・出力を得た")
    root.insert(3,"three")
    root.insert(5,"three")
    root.insert(8,"eight")
    root.prints()
    print("入力:9 出力:",root.search(9))
    print("入力:8 出力:",root.search(8))
    print("入力:7 出力:",root.search(7))
    print("入力:6 出力:",root.search(6))
    print("入力:5 出力:",root.search(5))
    print("入力:4 出力:",root.search(4))
    print("入力:3 出力:",root.search(3))
    print("入力:2 出力:",root.search(2))

def test2():
    root = Bintree()
    print("2. 下のような順番でinsertした時，以下のような入力・出力を得た")
    root.insert(5,"three")
    root.insert(3,"three")
    root.insert(8,"eight")
    root.prints()
    print("入力:9 出力:",root.search(9))
    print("入力:8 出力:",root.search(8))
    print("入力:7 出力:",root.search(7))
    print("入力:6 出力:",root.search(6))
    print("入力:5 出力:",root.search(5))
    print("入力:4 出力:",root.search(4))
    print("入力:3 出力:",root.search(3))
    print("入力:2 出力:",root.search(2))

def test3():
    root = Bintree()
    print("3. 下のような順番でinsertした時，以下のような入力・出力を得た")
    root.insert(8,"eight")
    root.insert(5,"three")
    root.insert(3,"three")
    root.prints()
    print("入力:9 出力:",root.search(9))
    print("入力:8 出力:",root.search(8))
    print("入力:7 出力:",root.search(7))
    print("入力:6 出力:",root.search(6))
    print("入力:5 出力:",root.search(5))
    print("入力:4 出力:",root.search(4))
    print("入力:3 出力:",root.search(3))
    print("入力:2 出力:",root.search(2))
test1()
test2()
test3()
