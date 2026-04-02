# 1

# 2
# 1 -> 1
# 2

# 3
# consider first step
# either one or two
# 1 -> 1 -> 1
#   -> 2
# 2 ->1

# 4
# 1 -> 1 -> 1 -> 1
#        -> 2 
#   -> 2 -> 1
# 2 -> 1 -> 1
# 2 -> 2

# 5
# 1 -> 1 -> 1 -> 1 -> 1
#             -> 2
#        -> 2 -> 1
#   -> 2 -> 1 -> 1
#        -> 2
# 2 -> 1 -> 1 -> 1
#        -> 2
#      2 -> 1


# 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            answer = 0
            n1 = 1
            n2 = 2
            for i in range(3, n + 1):
                answer = n1 + n2
                n1 = n2
                n2 = answer
            return answer
                
        
        