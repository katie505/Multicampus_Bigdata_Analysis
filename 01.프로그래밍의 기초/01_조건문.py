# 문제1
srp = input('가위, 바위, 보 중에서 입력하세요: ')
if srp == '가위':
  print('이겼다.')
elif srp == '바위':
  print('졌다.')
elif srp == '보':
  print('비겼다.')
else:
  print('잘못 입력했습니다.')
  
  
  # 문제2 - 1
birth = int(input('태어난 연도를 입력하세요: '))
age = 2022 - birth + 1

if age < 20:
  group = 10
elif age < 30:
  group = 20
elif age < 40:
  group = 30
elif age < 50:
  group = 40
elif age < 60:
  group = 50
elif age < 70:
  group = 60
elif age < 80:
  group = 70
elif age < 90:
  group = 80
elif age < 100:
  group = 90

print(f'나의 나이는 {age}입니다. {group}대입니다.')

group = age // 10

# 문제2 - 2
birth = int(input('태어난 연도를 입력하세요: '))
age = 2022 - birth + 1
group = (age // 10) * 10
print(f'나의 나이는 {age}입니다. {group}대입니다.')

# 문제3 - 1
score = input('점수를 입력하세요: ')

if score.isdigit() == True: # isnumeric보단 isdigit
  score = int(score)
  if score > 100 or score < 0:
    print('올바른 점수를 입력하세요.')
  elif score >= 90:
    print('A')
  elif score >= 80:
    print('B')
  elif score >= 70:
    print('C')
  elif score < 70:
    print('F')
else:
  print('잘못 입력했습니다.')
  
  # 문제3 - 2
score = input('점수를 입력하세요: ')

if score.isnumeric() == True:
  score = int(score)
  if score > 100 or score < 0:
    print('올바른 점수를 입력하세요.')
  elif score >= 90:
    print('A')
  elif score >= 80:
    print('B')
  elif score >= 70:
    print('C')
  elif score < 70:
    print('F')
else:
  print('잘못 입력했습니다.')
  
  # 문제3 - 3
score = input('점수를 입력하세요: ')

if score.isnumeric() == True:
  score = int(score)
  if score > 100 or score < 0:
    print('올바른 점수를 입력하세요.')
  elif score >= 90:
    print('A')
  elif score >= 80:
    print('B')
  elif score >= 70:
    print('C')
  elif score < 70:
    print('F')
else:
  print('잘못 입력했습니다.')
