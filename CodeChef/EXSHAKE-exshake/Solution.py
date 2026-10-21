n = int(input())
for _ in range(n):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    group = 0
    prefix = [0]*n 
    prefix[0] = arr[0]
    for i in range(1,n):
        prefix[i] = prefix[i - 1] + arr[i]
    for i in range(n):
        handshk = (prefix[i] * (prefix[i]-1))//2
        if handshk <= m:
            group = max(group,i + 1)
    print(group)
            