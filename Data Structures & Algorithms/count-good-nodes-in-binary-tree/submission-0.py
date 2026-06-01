# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        def dfs(root, path):
            if not root:
                return
            if len(path) == 0 or root.val >= max(path):
                ans[0] += 1
            
            if root.left:
                path.append(root.val)
                dfs(root.left, path)
                path.pop()
            
            if root.right:
                path.append(root.val)
                dfs(root.right, path)
                path.pop()

        
        dfs(root, [])
        return ans[0]
