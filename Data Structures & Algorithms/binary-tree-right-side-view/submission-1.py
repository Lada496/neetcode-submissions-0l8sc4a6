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
                cur = queue.popleft()
                if i == size - 1:
                    ans.append(cur.val)
                

                if cur.left:
                    queue.append(cur.left)
                
                if cur.right:
                    queue.append(cur.right)
                
                
        
        return ans
            
