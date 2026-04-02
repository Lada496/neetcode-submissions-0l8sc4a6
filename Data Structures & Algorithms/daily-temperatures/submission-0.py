class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n

        for i in range(n):
            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                tmp = stack.pop()
                ans[tmp[1]] = i - tmp[1]
            else:
                stack.append((temperatures[i], i))
        
        return ans
            