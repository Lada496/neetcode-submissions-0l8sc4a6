class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = curSum = 0
        hash = { 0: 1}

        for n in nums:
            curSum += n
            diff = curSum - k
            ans += hash.get(diff, 0)
            hash[curSum] = hash.get(curSum, 0) + 1
        
        return ans