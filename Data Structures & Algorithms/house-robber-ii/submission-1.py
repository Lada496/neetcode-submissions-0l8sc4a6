class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        def first():
            rob1, rob2 = 0,0

            for num in nums[:-1]:
                tmp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = tmp
            
            return rob2

        def last():
            rob1, rob2 = 0, 0

            for num in nums[1:]:
                tmp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = tmp
            
            return rob2
        
        return max(first(), last())
