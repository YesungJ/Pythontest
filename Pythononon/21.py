class TeamA:
    member = 0 #クラス変数
    def __init__(self,name,age):#初期化
        self.name = name 
        #self.name←クラスが持っているインスタンス変数
        self.age = age
        TeamA.member += 1
    def getBornYear(self):
        return 2019 - self.age


jang = TeamA("yesung", 27)
print(jang.name+"："+str(jang.age))
jang.name = "Jang Yesung"
print(jang.name)

takatsudi = TeamA("ayami", 25)
print("メンバーの人数"+str(TeamA.member))
print(jang.name+":"+str(jang.getBornYear())+"年生まれ")
