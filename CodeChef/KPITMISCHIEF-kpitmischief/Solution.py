t = int(input())
s = input()
ans_st = 0
ans_end = 0
start = -1
end = 0
diff = 0
for i in range(t):
    if s[i] == 'm' and start == -1:
        start = i
    elif s[i] == 'g':
        end = i - 1
        curr_diff = abs (end - start)
        if curr_diff > diff:
            diff = curr_diff
            ans_st = start
            ans_end = end
        start = -1
if start != -1:
    end = i 
    curr_diff = abs(end - start)
    if curr_diff > diff:
        ans_st = start
        ans_end = end
print(ans_st,ans_end)
        
        
    