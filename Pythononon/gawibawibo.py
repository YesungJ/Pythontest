#じゃんけんげーむ
#0=グー
#1=チョキー
#2=パー


from random import *
'''
count = list[1,2,3]

for triple in count:
    print(triple)

'''
hantei = int(0)
user = str(input("じゃんけんゲーム開始！\n"))
print("user:"+user)

if user == str("グー"):
    user = int(0)
elif user == str("チョキ"):
    user = int(1)
elif user == str("パー"):
    user = int(2)
#else :

com = randint(0,3)

#print(type(user))
#print(type(com))
if user == 0:
    if com == 0:
        hantei = 3
    elif com == 1:
        hantei = 1
    else:
        hantei = 2

elif user == 1:
    if com == 0:
        hantei = 2
    elif com == 1:
        hantei = 3
    else:
        hantei = 1

else:
    if com == 0:
        hantei = 1
    elif com == 1:
        hantei = 2
    else:
        hantei = 3

if com == 0:
    com = str("グー")
elif com == 1:
    com = str("チョキ")
elif com == 2:
    com = str("パー")
print("com:"+str(com))

hantei = hantei-1
if hantei == 0:
    print("user win")
elif hantei == 1:
    print("user lose")
elif hantei == 2:
    print("draw")