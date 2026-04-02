class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0] * n
        post = [0] * n
        maximum = 0
        for i in range(n):
            pre[i] = maximum
            maximum = max(maximum, height[i])
        
        maximum = 0
        for i in range(n - 1, -1, -1):
            post[i] = maximum
            maximum = max(maximum, height[i])
        
        ans = 0

        for i in range(n):
            curr = min(pre[i], post[i]) - height[i]
            if curr > 0:
                ans += curr
        
        return ans
