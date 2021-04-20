#Theory Chapter7 Returns
def p_plus(a, b):
  print(a+b)

def r_plus(a, b):
  return a+b

p_result = p_plus(2, 5)
#return none
r_result = r_plus(2, 5)
#return 7

print(p_result, r_result)

#function은 return하는 순간 그 다음은 실행 안한다!! 중요!!
#오직 하나의 값만 리턴 가능