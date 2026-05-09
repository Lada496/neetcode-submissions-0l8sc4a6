class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(i):
            if i == 0:
                return 1
            return i * factorial(i - 1)
        
        part1 = factorial(m + n -2)
        part2 = factorial(m-1) * factorial(n-1)
        return part1 // part2