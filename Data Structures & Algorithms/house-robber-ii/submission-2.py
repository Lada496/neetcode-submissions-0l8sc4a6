class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        def maxRob(nums: List[int]):
            rob1, rob2 = 0,0

            for num in nums:
                tmp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = tmp
            
            return rob2

        
        return max(maxRob(nums[:-1]), maxRob(nums[1:]))
