#LOOP
#for loop

days = ("mon", "tue", "wed", "thu", "fri")
'''
#1行ずつ
for day in days:
    #what is x -> なんでもいい
    print(day)
'''
#これも可能
'''
for number in [1, 2, 3, 4, 5]:
    print(number)
'''

for day in days:
    if day is "wed":
        break
    #抜ける
    else:
        print(day)