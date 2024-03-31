n,m = map(int, input().split())
nlist=list(map(int, input().split()))
mlist=list(map(int, input().split()))
merged =[]
counter_of_n =0
counter_of_m =0
 
while counter_of_n < n and counter_of_m < m:
    if nlist[counter_of_n] < mlist[counter_of_m]:
        merged.append(nlist[counter_of_n])
        counter_of_n+=1
    elif nlist[counter_of_n] > mlist[counter_of_m]:
        merged.append(mlist[counter_of_m])
        counter_of_m+=1
    else:
        merged.append(mlist[counter_of_m])
        merged.append(nlist[counter_of_n])
        counter_of_n+=1
        counter_of_m+=1
        
while counter_of_n < n:
    merged.append(nlist[counter_of_n])
    counter_of_n+=1
while counter_of_m < m:
    merged.append(mlist[counter_of_m])
    counter_of_m+=1
 
print(*merged)
