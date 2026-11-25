t = int(input())
for _ in range(t):
    n = int(input())
    arr = list (map(int,input().split()))
    maxi = max(arr)
    sumi = sum(arr)
    ans = 0
    for i in arr:
        d = 2 * i
        sumi += i
        if d > maxi:
            ans = max(sumi - d , ans)
        else:
             ans = max(sumi - maxi , ans)
        sumi -= i
    print(ans)