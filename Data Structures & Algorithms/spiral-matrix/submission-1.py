class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        visit = set()
        ans = []
        def dfs(r, c, direction):
            visit.add((r, c))
            ans.append(matrix[r][c])

            if len(visit) == ROWS * COLS:
                return

            dr, dc = direction
            nr, nc = r + dr, c + dc
            
            
            if nc == COLS or (direction == (0, 1) and (nr, nc) in visit):
                dfs(r + 1, c, (1, 0))
            elif nr == ROWS or (direction == (1, 0) and (nr, nc) in visit):
                dfs(r, c - 1, (0, -1))
            elif nc == -1 or (direction == (0, -1) and (nr, nc) in visit):
                dfs(r - 1, c, (-1, 0))
            elif direction == (-1, 0) and (nr, nc) in visit:
                dfs(r, c + 1, (0, 1))
            else:
                dfs(nr, nc, direction)
        
        dfs(0, 0, (0, 1))
        return ans