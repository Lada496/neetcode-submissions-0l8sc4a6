class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum = 0
        l = 0
        ans = 0

        for r in range(len(arr)):
            curSum += arr[r]
            print(r - l + 1)

            if r - l + 1 == k:
                avg = curSum / k
                if avg >= threshold:
                    ans += 1
                
                curSum -= arr[l]
                l += 1
        
        return ans