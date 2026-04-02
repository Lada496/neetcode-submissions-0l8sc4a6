# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1,2,3,4] -> [4,3,2,1]
# when prev = None, curr = 1
# curr.next -> None (prev),
# prev -> 1 (curr)
# curr -> 2 (curr.next)

# next round
# curr.next -> 1 (prev)
# prev -> 2 (curr)
# curr -> 3 (curr.next)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
            
        