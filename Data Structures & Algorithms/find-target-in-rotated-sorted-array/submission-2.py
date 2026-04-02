class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        pivot = l

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            m_actual = (m + pivot) % len(nums)
            if nums[m_actual] < target:
                l = m + 1
            elif nums[m_actual] > target:
                r = m - 1
            else:
                return (m + pivot) % len(nums)
        
        return -1

