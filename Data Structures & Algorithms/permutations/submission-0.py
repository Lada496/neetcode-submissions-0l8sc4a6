class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, visit):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num in visit:
                    continue
                
                # 1. Choose: add the number to path and visit set
                visit.add(num)
                path.append(num)
                
                # 2. Explore: recurse to find the next number
                backtrack(path, visit)
                
                # 3. Un-choose (Backtrack): remove the number to try other possibilities
                visit.remove(num)
                path.pop()
        
        backtrack([], set())
        return res