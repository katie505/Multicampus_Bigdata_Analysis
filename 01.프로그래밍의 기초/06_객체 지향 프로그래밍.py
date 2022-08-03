class Student:
  def __init__(self1, name, math, korean):
    self1.name = name
    self1.math = math
    self1.korean = korean

  def total_score(self1):
    self1.total = self1.math + self1.korean
    return self1.total

  def avg_score(self1):
    self1.avg = round(self1.total / 2, 1)
    return self1.avg

  def print_score(self1):
    return f'{self1.name}  {self1.total_score()}     {self1.avg_score()}'

  # def __str__(self):
  #   return f'{self.name}  {self.total_score()}     {self.avg_score()}'

students = [Student("김태희", 87, 98),
            Student("아이유", 92, 98),
            Student("아이린", 76, 96)]

print("이름", "총점", "평균", sep="\t")
for student in students:
  print(student.print_score())

#for student in students: #__str__로 하면 메소드를 굳이 적지 않아도 됨
#  print(student)


