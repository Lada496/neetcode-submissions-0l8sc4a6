class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()
        def backtrack(row, col, i):
            if i == len(word):
                return True
            
            if (row < 0 or row >= ROW or
                col < 0 or col >= COL or 
                (row, col) in visited or board[row][col] != word[i]):
                return False
            
            
            
            visited.add((row, col))
            
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = row + dr, col + dc
                if backtrack(nr, nc, i + 1):
                    return True
            
            visited.remove((row, col))
        
        for r in range(ROW):
            for c in range(COL):
                if (r, c) not in visited:
                    if backtrack(r, c, 0):
                        return True
        
        return False