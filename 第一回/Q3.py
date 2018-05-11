#問3 ボーリングの得点計算

#各ターンのスコアに分ける
def div_into_groups(scores):
    groups = []
    flag = False
    for i in range(len(scores)):
        if flag:
            flag = False
            continue
        if scores[i] == 10:
            groups.append([scores[i]])
        else:
            if i <= len(scores)-2:
                groups.append([scores[i], scores[i+1]])
                flag = True
            else:
                groups.append([scores[i]])

    return groups

#点数計算
def total_score(groups):
    total = 0
    for i in range(1,len(groups)):
        if i > 10 or i == 0:
            total += sum(groups[i])
            print(total)
        else:
            if groups[i-1] == [10]: #ストライク
                if groups[i] == [10]:
                    total += 20 + groups[i+1][0]
                else:
                    total += 10 + sum(groups[i])
            elif sum(groups[i-1]) == 10: #スペア
                total += 10 + groups[i][0]
            else:
                total += sum(groups[i-1])
    return total

def test1():
    scores = [10, 8, 2, 10, 0, 10, 10, 6, 4, 10, 8, 2, 10, 9, 1, 10]
    groups = div_into_groups(scores)
    print(total_score(groups) == 200)

def test2():
    scores = [1, 9, 8, 2, 10, 0, 10, 2, 6, 4, 1, 10, 8, 2, 10, 9, 1, 3]
    groups = div_into_groups(scores)
    print(total_score(groups) == 156)

def test3():
    scores = [1, 3, 8, 2, 3, 7, 1, 9, 10, 10, 10, 8, 2, 2, 8, 4, 6, 10]
    groups = div_into_groups(scores)
    print(total_score(groups) == 172)

test1()
test2()
test3()
