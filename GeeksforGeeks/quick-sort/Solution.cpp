class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot-1)
            self.quickSort(arr, pivot + 1, high)
        return arr
    def partition(self, arr, low, high):
        p = arr[low]
        i = low
        j = high
        while i < j:
            while arr[i] <= p and i < high:
                i += 1
            while arr[j] > p and j >= low + 1:
                j -= 1
            if i < j:
                arr[i],arr[j] = arr[j],arr[i]
        arr[low],arr[j] = arr[j],arr[low]
        return j
