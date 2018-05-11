#問5 安定結婚問題 Gale-Shapleyのアルゴリズム
def GS(m,w):
    matching = [None for i in m]
    while None in matching:
        for i in range(len(m)):
            if matching[i] != None:
                continue
            else:
                for j in m[i]:
                    if not j in matching:
                        matching[i] = j
                        break
                    else:
                        current_fiance = matching.index(j)   # wの既存の婚約者
                        if w[j].index(i) < w[j].index(current_fiance):
                            matching[i] = j
                            matching[current_fiance] = None
                            break
                        else:
                            continue
    return matching

def test1():
    men = [[1,0,2],[0,1,2],[0,1,2]]
    women = [[0,1,2],[2,0,1],[0,1,2]]
    print(GS(men, women) == [0,2,1])

def test2():
    men = [[1,0,2],[0,1,2],[0,2,1]]
    women = [[2,1,0],[2,0,1],[0,1,2]]
    print(GS(men, women) == [1,2,0])

test1()
test2()
