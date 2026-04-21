# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        queue = deque()
        
        if root:
            queue.append(root)
        

        while queue:
            size = len(queue)
            for i in range(len(queue)):
                if i == size - 1:
                    cur = queue.popleft()
                    ans.append(cur.val)
                else:
                    cur = queue.popleft()
                

                if cur.left:
                    queue.append(cur.left)
                
                if cur.right:
                    queue.append(cur.right)
                
                
        
        return ans
            
