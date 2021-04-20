#Theory Chapter6 Function Arguments 인자 -> 괄호 안에 넣는 거
#

def say_hello(who):
  print("hello", who)
  print("bye", who)


say_hello("jang")


def plus(a, b):
  print(a+b)

#default value
def minus(a, b=0):
  print(a-b)

plus(2, 5)
minus(2)