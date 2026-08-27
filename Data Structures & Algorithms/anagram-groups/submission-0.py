class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for st in strs:
            key = [0] * 26
            for ch in st:
                key[ord(ch) - ord('a')] += 1
            
            if tuple(key) in map:
                map[tuple(key)].append(st)
            else:
                map[tuple(key)] = [st]
            
        
        ans = []

        for value in map.values():
            ans.append(value)
        
        return ans