'''
class TeamA:
    member = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        TeamA.member += 1

jang = TeamA("yesung", 25)

jang.blood = "O"
print(jang.blood)

TeamA.teamname = "ultra"
print(TeamA.teamname)

#メソッドの追加
def getBlood(self):
    return self.blood
TeamA.getBlood = getBlood
print(jang.getBlood())

#アクセサメソッド
class TeamB:
    def __init__(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
    #プロパティ
    name = property(get_name)
    age = property(get_age, set_age)
#↑カプセル化
364396
jang = TeamB("yesung")
jang.set_age(25)
#print(jang.get_name()+str(jang.get_age()))

print(jang.name+str(jang.age))

'''

class TeamC:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    
    name = property(get_name)
    age = property(get_age, set_age)

#テストモジュール
if __name__ == "__main__":
    jang = TeamC("yesung")
    jang.age = 25
    print(jang.name+":"+str(jang.age))


from team import TeamC
kubota = TeamC("toshi")
print(kubota.name)
