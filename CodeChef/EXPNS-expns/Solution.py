n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    exp = b * 30
    if a >= exp:
        print('YES')
    else:
        print('NO')