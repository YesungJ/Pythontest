#print(3>2)
#print((1,2)>(2,1))


kimatsu = int(input("入力\n"))

if kimatsu > 100:
    print("正確な数字を入力してください")


elif kimatsu >=90:
    print("S")
    print("合格")

elif kimatsu >=80:
    print("A")
    print("合格")

elif kimatsu >=70:
    print("B")
    print("合格")

elif kimatsu >=60:
    print("C")
    print("合格")

else:
    print("D")
    print("不合格")