A=set(map(int,input().split()))
n=int(input())
isSuperSet=True
for i in range(n):
    N=set(map(int,input().split()))
    if not A.issuperset(N) or  A == N:
        isSuperSet=False
        break
print(isSuperSet)
