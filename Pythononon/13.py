'''
#リスト結合
list =["月","火"]+["水","木"]
print(list)
'''
'''
list =["mountain"]*4
print(list)
'''

'''
#スライス
print(list[::2])#2個飛ばし
'''

'''
#splitを使ってlistに変換
weekday ="mon, thu, wed, thr, fri, sat, sun"
weekday_list = weekday.split(",")
print(weekday_list)
'''
'''
#listの中の情報探し
weekday ="mon, thu, wed, thr, fri, sat, sun"
list = weekday.split(",")
print("mon" in list)
print("mon" not in list)
'''

'''
#indexで'ない場合'は例外処理
list=["mon","sun","wed","fri"]
print(list.index("fri"))
'''

'''
list=["mon","sun","wed","fri","satttt"]
list[4]="sat"
print(list)
#リストの追加
list.append("thu")
print(list)
'''
'''
#多次元リスト
nizi =["a",["b","c","d"],"e"]
print(nizi[0])
print(nizi[1][2])
print(nizi[2])
print(nizi[1])
'''
'''
#list要素削除
list=["mon","sun","thu","wed"]
list.remove("thu")
print(list)
#del
del list[1]
print(list)
#スライス
del list[0:1]
print(list)
'''
'''
list=[10,20,30,40,50,60,70,80,90,100]
print(max(list))
print(min(list))
print(sum(list))
'''

'''
#並び替え：sort
list=[10,20,30,40,50,60,70,80,90,100]
list.sort(reverse=True)
print(list)
list.sort()
print(list)
list2=sorted(list)
print(list)
print(list2)
list2 = sorted(list,reverse=True)
print(list2)
'''
#cmdのパラメータを取ることができる
import sys
for i in range(0,len(sys.argv)):
    print(sys.argv[i])