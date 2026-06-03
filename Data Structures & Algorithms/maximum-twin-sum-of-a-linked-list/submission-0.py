# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        tmp = slow
        slow = head
        fast = tmp

        prev = None
        while fast:
            next = fast.next
            fast.next = prev
            prev = fast
            fast = next
        
        fast = prev

        ans = 0
        while fast and slow:
            ans = max(ans, slow.val + fast.val)
            slow = slow.next
            fast = fast.next
        
        return ans