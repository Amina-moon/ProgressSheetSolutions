n, m = map(int, input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
left_of_arr1=left_of_arr2=0
smaller=[]
counter=0
while left_of_arr2 < len(arr2):
    if left_of_arr1 < len(arr1) and arr2[left_of_arr2] > arr1[left_of_arr1]:
        counter+=1
        left_of_arr1+=1
    else:
        smaller.append(counter)
        left_of_arr2+=1
print(*smaller)
