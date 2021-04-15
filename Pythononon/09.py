#配列を用意
sex = ["man","female"]

for sei in sex:
    print(sei)

#rangeオブジェクトを使ってカウント
for count in range(2):
    print(count+1)

#for 変数名 in 回す(カウント開始数字, カウント終了数字, 増やす数字)
#中身は1234
for cnt in range(1,5,1):
    print(cnt)

hatena = list(range(0,20,2))
print(hatena)


###ここからwhile
kazu = 10
cnt = 0
goukei = 0
while cnt <= kazu:
    goukei = goukei+cnt
    cnt=cnt+2
    print(goukei)
print(goukei)