#Theory Chapter2
#２つのシーケンスタイプ sequence type
#list tuple

days = ["mon", "tue" , "web", "thur","fri"]
print(type(days))
print("mon" in days)
print(days[3])
print(type(days[3]))
print(len(days))

#mutable == 変更できる？
#https://docs.python.org/ko/3/library/stdtypes.html#typesseq-mutable
#값을 바꾸고 싶지 않을때는 immutable sequence에 넣어라
# list는 sequence지만 mutable이다 
print(days)
days.append("sat")
print(days)
days.reverse()
print(days)