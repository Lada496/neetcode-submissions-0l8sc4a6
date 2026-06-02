class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        tmp = 0
        for i, n in enumerate(nums):
            tmp += n
            prefix[i] = tmp
        
        tmp = 0

        for i in range(len(nums) - 1, -1, -1):
            tmp += nums[i]
            postfix[i] = tmp

        for i in range(len(nums)):
            left = prefix[i - 1] if i - 1 >= 0 else 0
            right = postfix[i + 1] if i + 1 < len(nums) else 0

            print(left, right)

            if left == right:
                return i
        
        return -1
                