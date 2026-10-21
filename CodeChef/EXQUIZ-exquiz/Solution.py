def fn(n,s):
    ans = 0
    if s ==0:
        return  0
    if n == 1 and s != 4:
        return -1
    curr = 0
    for i in range(n):
        if curr < s:
            curr += 4
            ans += 1
        else:
            break
    ans += curr - s
    return ans
        

n = int(input())
for _ in range(n):
    n,s = map(int,input().split())
    print(fn(n,s))
    