class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        def find_ele(l,ele):
            r = n - 1
            p = -1
            while l <= r:
                mid = (l + r) //2
                if nums[mid] == ele:
                    p =  mid
                    r = mid - 1
                elif nums[mid] > ele:
                    r = mid - 1
                else:
                    l = mid + 1
            return p
        @cache
        def fn(i,val):
            currval = nums[i] + val
            length = 1
            j = find_ele(i + 1, currval + 1)
            if j != -1:
                length = max(length,1 + fn(j,0))
            j = find_ele(i + 1, currval)
            if j != -1:
                length = max(length,1 + fn(j,1))
            return length
        ans = 1
        for i in range(n):
            ans = max(ans,fn(i ,0),fn(i ,1))
        return ans