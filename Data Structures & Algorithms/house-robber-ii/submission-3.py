class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        def maxRob(start, end):
            rob1, rob2 = 0,0

            for i in range(start, end):
                num = nums[i]
                tmp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = tmp
            
            return rob2

        
        return max(maxRob(0, len(nums) - 1), maxRob(1, len(nums)))
