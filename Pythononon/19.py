#read
'''
file = open("Study19Data.csv","r",encoding="utf-8")
print("次の読み込み")
data = file.read()
print(data)
file.close()
'''

#readLines method
'''
file = open("Study19Data.csv")
data = file.readlines()
for d in data:
    print(d, end="")
file.close
'''

#readline method
'''
file = open("Study19Data.csv")
while True:
    data = file.readline()
    if data == "":
        break
    print(data,end="")
file.close
'''

#with文を使った処理
with open("Study19Data.csv") as file:
    while True:
        data = file.readline()
        if data == "":
            break
        print(data, end="")