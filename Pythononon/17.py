#可変長引数

def keisan(*kazu,mode):
    total=0
    if mode == "+":
        for i in kazu:
            total +=i
    if mode == "-":
        for i in kazu:
            total -= i
    return total
print(keisan(1,2,3,4,5,mode="+"))

print(keisan(1,2,3,4,5,mode="-"))

#引数の値を辞書で受け取る
def insert_data(**data):
    print(data)
insert_data(name="izawa",blood="A", age="43")

#lamda式
bigger = lambda kazu1, kazu2 : kazu1 if kazu1>kazu2 else kazu2
print(bigger(10,4))
print(bigger(100,400))

#2つ目でデフォルト値
getprice=lambda price,tax = 1.08 : int(price*tax)
print(getprice(1000))
print(getprice(1000,1.1))