# 問46 木に登録されたキーと値をキーが小さい順に表示するプログラム

class Bintree:
    def __init__(self,key=None,data=None): # デフォルト値を使うのはrootのみ
        self.key = key
        self.data = data
        self.left = None
        self.right = None
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
        print(self.to_s())
        if self.right != None:
            self.right.prints(d+1)

def test():
    root = Bintree()
    root.insert(11,"eleven")
    root.insert(5,"three")
    root.insert(3,"three")
    root.insert(7,"seven")
    root.insert(100,"a hundred")
    root.insert(2,"two")
    root.insert(19,"nineteen")
    root.insert(13,"thirteen")
    print("keyが小さい順に表示する")
    root.prints()
test()
