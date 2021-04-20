#Theory Chapter8 keyworded arguments
#밑에 a 나 b 같은 걸 포지셔널 알규멘트
#인자인데 위치에 의존적인 인자라는 뜻
def r_plus(a, b):
  return(a-b)

#位置ではなくargumentの名前で計算
result = r_plus(b = 30, a = 1)
print(result)

#stringの中に変数を入れたい場合は"の前にfを入れる
#次にnameに{}を入れる
def say_hello(name, age):
  return f"hello {name} you are {age} years old"

hello = say_hello(age="12", name="jang")
print(hello)