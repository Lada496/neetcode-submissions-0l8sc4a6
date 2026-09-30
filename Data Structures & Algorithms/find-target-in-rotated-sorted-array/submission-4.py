class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMinIndex():
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < nums[r]:
                    r = m
                else:
                    l = m + 1
            
            return l
        
        pivot = findMinIndex()

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            actual = (m + pivot) % len(nums)
            if nums[actual] < target:
                l = m + 1
            elif nums[actual] > target:
                r = m - 1
            else:
                return actual
        
        return -1