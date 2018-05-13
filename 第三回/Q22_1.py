#問22-1 与えられた要素に一番近い添え字を返す

def find(t,x):
    i = 0
    j = len(t)-1
    while i<=j:
        k = (i+j)//2
        #もしxと一致する要素があったら、その添え字を返す
        if t[k] == x:
            return k
        elif t[k] < x:
            i = k+1
        else:
            j = k-1
    #xと一致する要素がなかった場合,t[j]あるいはt[i]が一番近い
    if j == -1:
        return i
    elif i == len(t):
        return j
    elif x == (t[i]+t[j])/2:
        return [j,i]
    elif x - t[j] < t[i] - x:
        return j
    else:
        return i

def test():
    list = [1, 1.3, 2.1, 3.3, 3.9, 4.0, 5.1, 6.9, 8.3, 9.1]
    #7に一番近いのは6.9
    print(find(list, 7) == list.index(6.9))
    #1.15 に近いのは 1 と 1.3
    print(find(list, 1.15) == [list.index(1), list.index(1.3)])

test()
