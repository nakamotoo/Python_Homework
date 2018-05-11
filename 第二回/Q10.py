#問10 急行停車駅の間の駅数を求めたい
def express_gap(local, express):
    num = 0
    gap = []
    for i in range(len(local)):
        if i == 0:
            #始発駅はnumをappendしない
            continue
        elif local[i] not in express:
            num += 1
        elif local[i] in express:
            gap.append(num)
            num = 0
    return gap

def test():
    denentoshisen = ["渋谷駅","池尻大橋駅","三軒茶屋駅","駒沢大学駅","桜新町駅","用賀駅","二子玉川駅","二子新地駅","高津駅","溝の口駅","梶が谷駅","宮崎台駅","宮前平駅","鷺沼駅",
                    "たまプラーザ駅","あざみ野駅","江田駅","市が尾駅","藤が丘駅","青葉台駅","田奈駅","長津田駅","つくし野駅","すずかけ台駅","南町田駅","つきみ野駅","中央林間駅"]
    expressStops = ["渋谷駅","三軒茶屋駅","二子玉川駅","溝の口駅","鷺沼駅","たまプラーザ駅","あざみ野駅","青葉台駅","長津田駅","中央林間駅"]
    correct_answer = [1, 3, 2, 3, 0, 0, 3, 1, 4]
    print(express_gap(denentoshisen, expressStops) == correct_answer)

test()

#各停の駅数をNにした時の計算量: O(N^2)
#問8と同じく "elif local[i] not in express:" 部分の計算量に自信がないです…
