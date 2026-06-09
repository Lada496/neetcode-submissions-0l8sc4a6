class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_let = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        ans = []

        def backtrack(index, path):
            if index == len(digits):
                ans.append("".join(path))
                return
            print(num_to_let[int(digits[index])])
            
            for ch in num_to_let[int(digits[index])]:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()
        
        if len(digits) == 0:
            return []
        backtrack(0, [])
        return ans