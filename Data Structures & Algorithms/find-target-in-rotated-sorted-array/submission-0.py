class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        rot = l

        l, r = 0, len(nums)
        while l <= r:
            mid = (l + r) // 2
            real_mid = (mid + rot) % len(nums)
            if nums[real_mid] < target:
                l = mid + 1
            elif nums[real_mid] > target:
                r = mid - 1
            else:
                return real_mid
        
        return -1



