#type関数
'''
x=5
y=3.1
z="hello world"
print(type(x))
print(type(y))
print(type(z))
'''
'''
x="HellO"
#小文字化
print(x.lower())
print(len(x))

#ループも可
for c in x:
    print(c)
'''
#スライス
'''
x="yesung"

print(x[0:2])
print(x[:3])
print(x[2:])
'''
'''
#文字があるかどうか検索
x="abcdefga"
print("a"in x)
#find関数：ない場合は-1 ある場合文字の位置を教えてくれる
print(x.find("a"))
'''
#format関数
x=18
y="成人"
print("{}歳は{}です。".format(x,y))
#順番変え
print("{1}は{0}歳です。".format(x,y))

#3桁くくり
print("{0:,}".format(1000000))




