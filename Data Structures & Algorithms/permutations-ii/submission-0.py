class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for j in range(len(nums)):
                if used[j]:
                    continue
                if j > 0 and nums[j] == nums[j-1] and not used[j-1]:
                    continue
                used[j] = True
                path.append(nums[j])
                backtrack(path)
                path.pop()
                used[j] = False

        backtrack([])
        return res
                
