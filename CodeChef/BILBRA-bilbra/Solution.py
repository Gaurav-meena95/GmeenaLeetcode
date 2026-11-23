def fn(arr, student , mid):
    stu = 1
    curr_page = 0
    for i in arr:
        if curr_page + i <= mid:
            curr_page += i
        else:
            stu += 1
            curr_page = i
            if stu > student:
                return False
    return True
        

t = int(input())
for _ in range(t):
    n,a = map(int,input().split())
    arr = list(map(int,input().split()))
    low = max(arr)
    high = sum(arr)
    ans = high
    while low <= high:
        mid = (low + high ) // 2
        if fn(arr, a , mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)