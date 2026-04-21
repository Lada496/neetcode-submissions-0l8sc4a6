class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        ROWS, COLS = len(image), len(image[0])
        visited = set()
        st_col = image[sr][sc]

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or image[r][c] != st_col:
                return
            
            visited.add((r, c))
            image[r][c] = color
            
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        dfs(sr, sc)
        
        return image

