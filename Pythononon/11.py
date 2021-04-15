
#age = int(input("input your age"))
#exceptionも可能
#終了ライブラリ
'''
import sys
try:
    age = int(input("input your age\n"))
except:
    print("that was string")
    sys.exit()
'''
#-------------#
import sys
try:
    age = int(input("input your age\n"))
except:
    print("that was string")
    sys.exit()
else:
    if age >= 18:
        print("seinen")
    else:
        print("miseinen")