#about module
#機能の集合　importで使える
#よくつかわれるもの　datetime
#쓸것만 importing하는 게 좋다
'''
import math 

#올림값 반환
print(math.ceil(1.2))
print(math.ceil(3))

#絶対値
print(math.fabs(-1.2))

'''
#必要な機能のみもってくるとき
from math import ceil, fsum, fabs 

print(ceil(3.1))
#fsum
print(fsum([1,2,3,4,5,6,7,8,9,10]))

#module 名前変更
#from math import fsum as sexy_sum
#print(saxy_sum([1,3,5]))


#다른 파일에 저장된것도 임포트 할 수 있다!!
#calculation.py 를 
#from calculation improt plus -> calculation.py의 def plusr기능을 가져옴
