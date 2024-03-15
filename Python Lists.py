if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        a=input().split()
        if a[0] == 'insert':
            i=int(a[1])
            e=int(a[2])
            lst.insert(i,e)
        elif a[0] == 'print':
            print(lst)
        elif a[0] == 'remove':
            e=int(a[1])
            lst.remove(e)
        elif a[0] == 'append':
            e=int(a[1])
            lst.append(e)
        elif a[0] == 'sort':
            lst.sort()
        elif a[0] == 'pop':
            lst.pop()
        else:
            lst.reverse()
