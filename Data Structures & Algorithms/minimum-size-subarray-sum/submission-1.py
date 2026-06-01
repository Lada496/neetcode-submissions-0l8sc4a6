class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        curSum = 0
        ans = float("inf")

        while r < len(nums):
            curSum += nums[r]

            while curSum >= target and l <= r:
                ans = min(r - l + 1, ans)
                curSum -= nums[l]
                l += 1
            
            r += 1
        
        return ans if ans != float("inf") else 0