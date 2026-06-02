class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for r in range(len(matrix)):
            tmp = []
            cur = 0
            for c in range(len(matrix[0])):
                cur += matrix[r][c]
                tmp.append(cur)
            
            self.prefix.append(tmp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row2 - row1 + 1):
            preLeft = self.prefix[row1 + i][col2]
            preRight = self.prefix[row1 + i][col1 - 1] if col1 - 1 >= 0 else 0

            ans += preLeft - preRight
        
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)