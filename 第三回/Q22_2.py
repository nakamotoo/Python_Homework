#問22-2 上下eの範囲に入る要素の添え字の最大値と最小値

def find(t,x,e):
    #添え字の最大値maxを求める
    i = 0
    j = len(t)-1
    max = None
    while i<=j:
        k = (i+j)//2
        #x+eとぴったり等しい要素があった場合
        if t[k] == x+e:
            max = k
            break
        elif t[k] < x+e:
            i = k+1
        else:
            j = k-1
    #x+eとぴったり等しい要素がなかった場合
    if max is None:
        if j >= 0:
            max = j
        #x+eがリストの最小の要素を下回った場合
        else:
            return None

    #添え字の最小値minを求める
    i = 0
    j = len(t)-1
    min = None
    while i<=j:
        k = (i+j)//2
        #x-eとぴったり等しい要素があった場合
        if t[k] == x-e:
            min = k
            break
        elif t[k] < x-e:
            i = k+1
        else:
            j = k-1
    #x-eとぴったり等しい要素がなかった場合
    if min is None:
        # x-eがリスト内の最大の要素を超えてしまった場合
        if i == len(t):
            return None
        # x-eがt[j]とt[i]の間にある場合、iが最小の添え字
        else:
            min = i
        if min > max:
            return None
    return [min, max]


def test():
    list = [1, 1.3, 2.1, 3.3, 3.9, 4.0, 5.1, 6.9, 8.3, 9.1]
    #1-7の要素のindexは0-7
    print(find(list, 4, 3) == [0,7])
    #99-101の要素はない
    print(find(list, 100, 1) == None)

test()
