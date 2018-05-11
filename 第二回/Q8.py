#問8 各駅のリストと急行のリストから急行の止まらない駅のリストを作る
def only_local(local, express):
    only_local = []
    for i in local:
        if i not in express:
            only_local.append(i)
    return only_local

def test():
    inokashira = ["渋谷駅","神泉駅","東大前駅","駒場駅","池ノ上駅","下北沢駅","新代田駅","東松原駅","明大前駅","永福町駅","西永福駅","浜田山駅","高井戸駅","富士見ヶ丘駅","久我山駅","三鷹台駅","井の頭公園駅","吉祥寺駅"]
    inokashiraExpress = ["渋谷駅","下北沢駅","明大前駅","永福町駅","久我山駅","吉祥寺駅"]
    correct_answer = ['神泉駅', '東大前駅', '駒場駅', '池ノ上駅', '新代田駅', '東松原駅', '西永福駅', '浜田山駅', '高井戸駅', '富士見ヶ丘駅', '三鷹台駅', '井の頭公園駅']
    print(only_local(inokashira, inokashiraExpress) == correct_answer)

test()

#各停の駅数がNとした時の計算量：O(N^2)
#"if i not in express"の部分の計算量がO(N)なのかどうか自信がないです…(expressの駅数をMとしたらO(M)??)

#O(MN)
