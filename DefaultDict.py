from collections import defaultdict

n,m=map(int,input().split())
d = defaultdict(list)
for i in range(n):
    words_of_n=input()
    d[words_of_n].append(i+1)
for i in range(m):
    word_of_m = input()
    if word_of_m in d:
        print(' '.join(str(value) for value in d[word_of_m]))
    else:
        print('-1')
