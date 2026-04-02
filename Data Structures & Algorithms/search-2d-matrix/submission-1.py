class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # Find the correct row using binary search
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                # Target is within the range of this row
                row = matrix[mid]
                break
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
        else:
            # Target is not in any row
            return False

        # Binary search within the row
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False




        