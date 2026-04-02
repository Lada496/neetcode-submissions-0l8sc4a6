# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        # merge lists[0] and lists[1]
        l = lists[0]
        r = lists[1]

        new = ListNode()
        cur = new

        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        
        while l:
            cur.next = l
            l = l.next
            cur = cur.next
        
        while r:
            cur.next = r
            r = r.next
            cur = cur.next
        
        newLists = lists[2:]
        newLists.insert(0, new.next)

        return self.mergeKLists(newLists)
        