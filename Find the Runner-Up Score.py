if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    m=sorted(arr)
    for i in range(len(m)-1,-1,-1):
        if m[i] != m[len(m)-1]:
            print(m[i])
            break
