'''
bin = []
for n in range(0,17,1):
    bin.append(2**n)
print(bin)

bin = [2**n for n in range(0,17,1)]
print(bin)

#リストをもとにリストをつくる
price=[100,250,300]
tax = 1.1
total = [int(p*tax) for p in price]
print(total)

#文字列
rank = [r + "ランク" for r in "ABCDEF"]
print(rank)
'''

#条件を満たす用件だけを
'''
gusuu = [c for c in range(0,10,1) if c % 2 ==0]
print(gusuu)

citys = ["鳥取県米子市","鳥取県境港市","広島県福山市","広島県広島市"]
tottori_citys = [city[3:] for city in citys if city.startswith("鳥取県")]
print(tottori_citys)
'''
'''
#リストの中にタプルを入れてその中の情報と
test = [("A","合格"),("B","合格"),("C","不合格"),("D","合格")]
passed= [x[0] for x in test if x[1] == "合格"]
print(passed)
'''
'''
#辞書の活用
teams = ["A","B"]#リスト
team_dic = {t:0 for t in teams}
print(team_dic)
points = [40,59]
team_dic = {t:p for t,p in zip(teams,points)}
print(team_dic)

#入れ替え
team_dic={str(p):t for (t,p) in team_dic.items()}
print(team_dic)
'''

#集合の内包表記
point = [10,10,20,100,40,50,60]
fails = {x for x in point if x<= 60}
print(fails)