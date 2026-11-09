# update the code below to solve this problem

import math

t = int(input())
for i in range(t):
    a,o = map(int,input().split())
    ans = math.gcd(a,o)
    print(ans)
    
