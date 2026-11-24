class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        arr1 = []
        s = []
        arr2 = []
        for i in nums:
            if i < pivot:
                arr1.append(i)
            elif i == pivot:
                s.append(i)
            else:
                arr2.append(i)
        return arr1 + s + arr2