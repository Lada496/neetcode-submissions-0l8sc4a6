class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Map = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for n in nums2:
            while stack and n > stack[-1]:
                val = stack.pop()
                idx = nums1Map[val]
                res[idx] = n
            if n in nums1Map:
                stack.append(n)
        
        return res