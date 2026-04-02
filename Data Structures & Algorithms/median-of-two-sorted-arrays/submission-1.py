class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        harf = (m + n + 1) // 2
        l, r = 0, m

        while l <= r:
            mid = (l + r) // 2
            nums2_m = harf - mid
            
            maxLeft1 = nums1[mid - 1] if mid > 0 else float('-inf')
            minRight1 = nums1[mid] if mid < m else float('inf')
            
            maxLeft2 = nums2[nums2_m - 1] if nums2_m > 0 else float('-inf')
            minRight2 = nums2[nums2_m] if nums2_m < n else float('inf')
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                r = mid - 1
            else:
                l = mid + 1