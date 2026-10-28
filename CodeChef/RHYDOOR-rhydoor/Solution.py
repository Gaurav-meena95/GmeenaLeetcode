def fn(n,s):
    if n < 3:
        return 0
    ans = 0
    i = 0
    while i < n-2:
        if s[i] == s[i + 1] == s[i+2]:
            ans += 1
            i += 3
        else:
            i += 1
    return ans
    
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(fn(n,s))
    
            