#問15 二次元の座標を整列する

class Loc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def test():
    with open("loc.dat") as f:
        buf=f.readlines()
    loc=[Loc(float(buf[i].split(",")[0]),float(buf[i].split(",")[1])) for i in range(len(buf))]
    loc.sort(key=lambda obj: (obj.x, obj.y))
    print("最初の50組をprintして確認してみる")
    for i in range(50):
        print(loc[i].x,loc[i].y)
test()
