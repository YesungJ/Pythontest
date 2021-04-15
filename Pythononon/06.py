x = 5
y = 3.4
z = "hello \"jang\""
z2 = "hello \n yesung"
#何型なのか表示するtype
#print(type(x))
#print(type(y))
#ダブルコーテーション　\"
#改行 \n
#print(z)
#print(z2)

#--リスト--
name = ["takahashi", "jang", "sugiyama"]
print(name[0])

name[0]="yeajin"
print(name[0])

print(len(name))

#---タプル--
season = "sprint", "summer", "fall", "winter"
#以下でもおっけー
weekday=("sunday", "satuerday")
print(season)
print(weekday)

#ID関数 各個人番号表示
print(id(season[0]))