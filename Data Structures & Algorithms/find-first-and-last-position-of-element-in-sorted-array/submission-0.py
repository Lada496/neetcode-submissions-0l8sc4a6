class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        l, r = 0, len(nums) - 1

        # first occurence if exist
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        if l in range(len(nums)) and nums[l] == target:
            res[0] = l
        
        l, r = 0, len(nums) - 1
        # last
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        
        if r in range(len(nums)) and nums[r] == target:
            res[1] = r
        
        return res