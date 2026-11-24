class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        if not head:
            return None
            
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
            
        a1 = []
        a2 = []
        for i in arr:
            if i < x:
                a1.append(i)
            else:
                a2.append(i)
                
        ans = a1 + a2
        a = ListNode(ans[0])
        curr = a
        for i in range(1, len(ans)):
            curr.next = ListNode(ans[i])
            curr = curr.next
            
        return a