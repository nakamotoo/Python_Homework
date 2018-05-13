#問21 pg10の各単語の出現回数を調べる

def counter(sorted, unique):
    #単語と回数を格納するリスト
    counts = []
    k = 0
    for i in range(len(unique)):
        counts.append([unique[i], 0])
        while k < len(sorted) and sorted[k] == unique[i]:
            counts[i][1] += 1
            k += 1
    return counts

with open("pg10sorted.dat") as f:
    buf = f.readlines()
sorted = [buf[i].strip() for i in range(len(buf))]
with open("pg10uniq.dat") as f:
    buf = f.readlines()
unique = [buf[i].strip() for i in range(len(buf))]

counts = counter(sorted,unique)
#最初の10個を確認してみる
for i in range(10):
    print(counts[i])
