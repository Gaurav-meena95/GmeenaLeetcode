t = int(input())
for _ in range(t):
    n , k = map(int,input().split())
    s = input()
    ans = 0
    i = 0
    while i < n:
        if s[i] == "1":
            p = min(n,i+k)
            ans += 1
            i = p + 1
        else:
            i += 1
    print(ans)