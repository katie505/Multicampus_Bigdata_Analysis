# 노래 가사에 Yesterday가 몇번 나오나
f = open('yesterday.txt', 'r')
yesterday_lyric = f.readlines() 
f.close

contents = ""
for line in yesterday_lyric:
  contents = contents + line.strip() + '\n'
  
n_yesterday = contents.upper().count('YESTERDAY')
print("Number of a Word 'Yesterday'", n_yesterday)


# 노래 가사 속 단어들의 빈도수
lyrics = lyrics.replace("\n", " ")
lyrics = lyrics.lower().split()
from collections import defaultdict

word_count = defaultdict(lambda: 0) # default값을 0으로
for word in lyrics:
  word_count[word] += 1

from collections import OrderedDict

for i, j in OrderedDict(sorted(word_count.items(), key = lambda t: t[1], reverse = True)).items():
  print(i, j)
