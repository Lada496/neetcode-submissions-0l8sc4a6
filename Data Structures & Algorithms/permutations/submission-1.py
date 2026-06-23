class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i == len(nums):
                return [[]]
            
            resParam = []
            params = helper(i + 1)

            for p in params:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    resParam.append(pCopy)
            
            return resParam
        
        return helper(0)
        