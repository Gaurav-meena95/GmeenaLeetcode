t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        val = int(s[i-1] + s[i])
        if val % 4 == 0:
            ans += 1
    print(ans)
        
    