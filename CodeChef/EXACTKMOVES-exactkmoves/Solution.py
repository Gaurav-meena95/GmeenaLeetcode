def fn(n,k):
    if k > n:
        return 'NO'
    if n <= k * 2:
        return 'YES'
    else:
        return 'NO'
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    print(fn(n,k))
