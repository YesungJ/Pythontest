'''
def getPrice(price,tax):
    return int(price*tax)

print(getPrice(100,1.08))

print(getPrice(100,tax=1.08))
#print(getPrice(price=100,1.08)) #エラー
'''
'''
#デフォルト値を設定
def getPrice(price, tax=1.08):
    return int(price*tax)

print(getPrice(1000))
'''

'''
#ミュータブルなオブジェクト
list = ["A", "B"]
def add(list_item):
    list_item.append("c")
add(list)
print(list)
'''

#グローバル変数の利用
x = 0
def setcount(y):
    x=y
def setcount2(y):
    global x
    x=y
    #一番上のx

setcount(10)
print(x)
setcount2(12)
print(x)

#returnで戻す値を作る