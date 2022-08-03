# 삼각형의 밑변과 높이를 입력받은 후 삼각형의 면적을 계산하는 함수
def triangle_area(base, height):
  area = base*height/2
  print(f'삼각형의 밑변 : {base}\n삼각형의 높이 : {height}\n삼각형의 넓이는 {area}입니다.')

triangle_area(3, 4)


# 두개의 정수를 받아서 평균을 구하는 함수
def myavg(x, y):
  avg = (x + y) / 2
  return avg

myavg(1, 2)


# AND 연산자를 함수로 만들어 보세요
def and_fun(a, b):
  if a == b:
    if a == True:
      return 1
    else:
      return 0
  else:
    return 0

print(and_fun(0,0))
print(and_fun(0,1))
print(and_fun(1,0))
print(and_fun(1,1))


# OR연산자를 함수로 만들어 보세요
def or_fun(a, b):
  if a == b:
    if a == True:
      return 1
    else:
      return 0
  else:
    return 1

print(or_fun(0,0))
print(or_fun(0,1))
print(or_fun(1,0))
print(or_fun(1,1))


# XOR GATE 를 활용하여 XOR 연산자를 위에서 작성한 and_fun과 or_fun 의 합성함수로 만들어 보세요
def xor_fun(a, b):
  if and_fun(a, b) != or_fun(a, b):
    return 1
  else:
    return 0


print(xor_fun(0,0))
print(xor_fun(1,1))
print(xor_fun(1,0))
print(xor_fun(0,1))
