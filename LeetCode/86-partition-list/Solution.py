class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        if not head:
            return None
            
        before_head = ListNode(0)
        after_head = ListNode(0)
        before = before_head
        after = after_head
        
        curr = head
        while curr:
            if curr.val < x:
                before.next = ListNode(curr.val)
                before = before.next
            else:
                after.next = ListNode(curr.val)
                after = after.next
            curr = curr.next
            
        before.next = after_head.next
        return before_head.next