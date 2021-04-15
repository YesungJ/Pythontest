#スーパークラスをtukuru
class animal:
    def __init__(self,animal_type,tall):
        self.__animal_type = animal_type
        self.__tall = tall

    def getAnimalType(self):
        return self.__animal_type

    def getTall(self):
        return self.__tall
    animal_type = property(getAnimalType)
    tall = property(getTall)
#ここまで

#ここからサブクラス
class human(animal):
    def __init__(self, animal_type, tall):
        super().__init__(animal_type, tall)

    def aisatsu(self):
        print("hello")

#インスタンス
lion = animal("ライオン", 50)
print(lion.animal_type+":"+str(lion.tall)+"cm")
jang = human("人間", 180)
print(jang.animal_type+":"+str(jang.tall)+"cm")
jang.aisatsu()
