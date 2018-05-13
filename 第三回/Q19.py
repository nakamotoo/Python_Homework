#問19 二分探索法で探したいものが見つからない場合

#二分探索法の定義
def find(t,s):
    i = 0
    j = len(t)-1
    while i<=j:
        k = (i+j)//2
        if t[k]==s:
            return k
        elif t[k] < s:
            i = k+1
        else:
            j = k-1
    #見つからない場合[i,j]を返す
    return [i,j]
#0-99のリスト
list = [i for i in range(100)]
#100を探す
print(find(list,100)) #[100,99]
#101を探す
print(find(list,101)) #[100,99]
#-1を探す
print(find(list,-1)) #[0,-1]
#-2を探す
print(find(list,-2)) #[0,-1]
#結論
#リスト(最大の添え字をmaxIndexとする)の最大値より大きいものを探した場合、[i,j] = [ maxIndex+1,maxIndex ]となって終わる
#リストの最小値より小さいものを探した場合、[i,j] = [0, -1]となって終わる
#つまり、常に j = i-1 で終わるが、i,jは配列の範囲外の添え字になりうる(maxIndex+1や-1)
