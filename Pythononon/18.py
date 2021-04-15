'''
#map関数
def gettaxprice(price,tax=1.10):
    return int(price*tax)

prices = [100,250,300,1000]

for price in map(gettaxprice,prices):
    print(price)

ontaxprices = list(map(gettaxprice, prices))
print(ontaxprices)
'''
'''
#無名関数を使ったマップ関数
prices = [100,250,300,1400]
ontaxprices = list(map(lambda price, tax=1.10:int (price*tax),prices))
print(ontaxprices)

#マップ関数の代わりに内包表記
prices = [100,250,300,1400]
ontaxprices = [int(price * 1.10) for price in prices]
print(ontaxprices)
'''
'''
#filter関数
def over1000(price):
    return price >= 1000

prices = [100, 200, 300, 1400]
for price in filter(over1000,prices):
    print(price)

#lambda式
def over1000(price):
    return price >=1000

prices = [100,200,300,1400]
for price in filter(lambda price:price>=1000,prices):
    print(price)


#内包表記
prices = [100,200,300,1400]
over1000prices = [price for price in prices if price >= 1000]
print(over1000prices)

#辞書のソート
teams = {"zaku":"ateam","bash":"ateam","ken":"bteam","take":"ateam"}
print("名前の昇順")
for player in sorted(teams.items(),key=lambda k:k[0]):
    print(player[0],player[1])

print("名前の降順")
for player in sorted(teams.items(),key=lambda k:k[1]):
    print(player[0],player[1])

#ジェネレータ関数
def weekdays():
    wdays=["sun","mon","wed","thu","fri","sat"]
    for w in wdays:
        yield w
w = weekdays()
print(next(w))
print(next(w))
print("一休み")
w=weekdays()
for x in w:
    print(x)
'''
#内包表記との違いは括弧が違うメモリ効率が違う
wdays=["sun","mon","wed","thu","fri","sat"]
w = (w for w in wdays)
for x in w:
    print(x)



