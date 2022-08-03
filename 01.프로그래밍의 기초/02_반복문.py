## For문

# 1단부터 9단까지 한번에 출력하도록 작성해보세요
for i in range(1, 10):
  print(f'====={i}단=====')
  for j in range(1, 10):
    print(f'{i} x {j} = {i*j}')
    
    
seasons = ['봄', '여름', '가을', '겨울']
season1 = '겨울'

for season2 in seasons:
  if season2 == season1:
    print('아 겨울 진짜 추워 죽겠다')
  else:
    print(f'현재 계절은 {season2}이 아닙니다')
    
    
for i in range(5):
 print('★', end="")
  
  
for i in range(4):
 for j in range(5):
   print('★', end = "")
 print() #공백 출력
  
  
for i in range(1,6):
 for j in range(i):
   print('★', end = "")
 print()
  
  
for i in range(1,6):
 for j in range(6-i):
   print('★', end = "")
 print()
  
  
for i in range(1,6):
  print('☆'*(5-i),'★'*i, sep = '')
    
    
for i in range(1,6):
  print(" "*(5-i),'★'*i)
  
  
apart=[[1001, 1002, 1003, 1004, 1005, 1006],[2001, 2002, 2003, 2004, 2005, 2006], [3001, 3002, 3003, 3004, 3005, 3006], [4001, 4002, 4003, 4004, 4005, 4006]]
refusal = [1001,2006,3005,4004]

for x in apart:
  for family in x:
    if family in refusal:
      continue
    else:
      print(f'신문 배달: {family}')
      
      
 #-------------------------------------------------------------------------------------------------------
 ## While문
 
 import random
srp = ['가위', '바위', '보']
answer = random.choices(srp, k = 10)

win = 0
lose = 0
draw = 0
i = 0

while i < 10:
  srp1 = input('가위, 바위, 보: ')
  if srp1 not in srp:
    print('잘못내셨습니다.')
  else:
    if srp1 == answer[i]:
      print('비겼습니다.')
      draw += 1

    elif (srp1 == '가위' and answer[i] == '보') or\
      (srp1 == '바위' and answer[i] == '가위') or\
      (srp1 == '보' and answer[i] == '바위'):
      print('이겼습니다.')
      win += 1

    else:
      print('졌습니다.')
      lose += 1
  
  i += 1
      

print(f'승:{win}\n패:{lose}\n비김:{draw}')


