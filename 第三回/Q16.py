#問16 整列によって元のデータがどこに移ったか求める

def simplesort(a):
    #インデックスの配列を作る
    index = [i for i in range(len(a))]
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[j] < a[min]:
                min = j
        a[i],a[min] = a[min],a[i]
        #aの要素を入れ替えると同時に,index配列の要素も入れ替える
        index[i],index[min] = index[min], index[i]
    return index

#資料の例で確かめる
def test():
    a = [2,2,1,1]
    print(simplesort(a) == [2,3,0,1])

test()
