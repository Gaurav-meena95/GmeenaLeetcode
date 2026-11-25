t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    r,c = map(int,input().split())
    arr = [(1,1),(1,m),(n,1),(n,m)]
    reach = float('inf')
    for i,j in arr:
        reach = min(reach,max(abs(r-i),abs(c-j)))
    ans = reach +  2 * min(m,n) + max(m,n) - 3
    print(ans)
        