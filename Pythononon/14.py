#key = jan, feb, mar
#value = 1gatsu, 2gatsu, 3gatsu
#months = {"jan":"1月","Feb":"2月","Mar":"3月"}

#print(len(months))
#print(months["Feb"])

#要素の追加
#months["Apr"] = "4月"
#print(months)

#追加した順番に表示されることが保障されるわけではない

#キーの削除
#del(months["Feb"])
#print(months)

#辞書の中にないkeyをdelするときは例外が発生

#そのキーが存在するかどうか確認方法
#print("Feb" in months)
#print("Apr" in months)

#キーとvalueの一覧表示
#print(months.keys())
#print(months.values())

#キーとvalueのペアを取ってくる items
#print(months.items())

#一個ずつとってくる
#for en,jp in months.items():
#    print("英語:{} 日本語:{}".format(en,jp))

#ここから集合
#順番は保障されない
'''
months = {"1月","2月","3月","4月","1月"}
print(months)
for x in months:
    print(x)

#リストから集合の作成も可
list = [1,2,3,4,5,6,1,2,3]
#重複する値だけlistに入る
sets = set(list)
print(sets)
sets.add(100)
print(sets)
sets.remove(1)
sets.clear()
print(sets)
'''
kazu={1,2,3,4,5,6,7,8,9,10}
kisuu={1,3,5,7,9,11,15}
#どっちかにある
print(kazu | kisuu)
#両方にある
print(kazu & kisuu)
#奇数を含まれない
print(kazu - kisuu)
#一方にだけ含まれる要素
print(kazu ^ kisuu)
