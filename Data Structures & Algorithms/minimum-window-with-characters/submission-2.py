class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        t_count = Counter(t)
        sub_count = Counter()
        required = len(t_count)
        formed = 0
        i = 0
        for j in range(len(s)):
            ch = s[j]
            sub_count[ch] += 1
            if ch in t_count and sub_count[ch] == t_count[ch]:
                formed += 1
            
            while i <= j and formed == required:
                sub = s[i:j+1]
                if ans == "" or len(sub) < len(ans):
                    ans = sub
                
                left_ch = s[i]
                sub_count[left_ch] -= 1
                if left_ch in t_count and sub_count[left_ch] < t_count[left_ch]:
                    formed -= 1
                i += 1
        
        return ans