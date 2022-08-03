# 과목과 점수를 입력받고 평균을 내어주는 함수를 만들어보세요

# 방법1
def avg_cal():
  total = {}
  while True:
    subject = input('과목 : ')
    score = int(input('점수 : '))
    answer = input('추가하실건가요?\n  예 or 아니요 : ')
    total[subject] = score
    if answer == '예':
      continue
    elif answer == '아니요':
      for key in total:
        print(f'{key} : {total[key]}')
      print(f'평균 : {round(sum(total.values()) / len(total), 1)}')
      break

# 방법2
def avg_cal():
  subject_list = []
  score_list = []
  while True:
    subject = input('과목 : ')
    score = int(input('점수 : '))
    answer = input('추가하실건가요?\n  예 or 아니요 : ')
    subject_list.append(subject)
    score_list.append(score)

    if answer == '예':
      continue
    elif answer == '아니요':
      for sub, sco in zip(subject_list, score_list):
        print(f'{sub} : {sco}')
      avg = sum(score_list) / len(sub)
      print(f'평균 : {round(avg, 1)}')
      break
      
      
 # 1000미만의 숫자중에 3과 5의 배수의 합을 구하는 함수
def total_35():
  sum = 0
  for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
      sum += n
  return sum

total_35()


# 1000미만의 숫자중에 n과 m을 입력받고 n과 m의 배수의 합을 구하는 함수
def total(n, m):
  sum = 0
  for i in range(1, 1000):
    if i % n == 0 or i % m == 0:
      sum += i
  return sum

total(3, 5)


def total(n, m):
  result_nm = [i for i in range(1, 1000) if i%n == 0 or i%m == 0]
  return sum(result_nm)

total(3, 5)


# 1부터 n까지의 합을 재귀함수를 이용해 구현해보기
def total(n):
  if n == 1:
    return 1
  else:
    return n + total(n-1)

total(100)


# x^n(x를 n번 곱하는 재귀함수) 구현
def x_n(x,n):
  if n == 0:
    return 1
  else:
    return x_n(x, n-1)*x
x_n(2,4)


# 피보나치 수열
def fibo(n):
  if n == 0:
    return 1
  elif n == 1 or n == 2:
    return 1
  else:
    return fibo(n-1) + fibo(n-2)
  
  
# 최대공약수를 구할 수 있는 유클리드 알고리즘
def gcd(n, m):
    if m == 0:
      return n
    else:
      return gcd(m, n%m)

gcd(12, 15)
