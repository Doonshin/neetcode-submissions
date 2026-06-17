class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char_map = {}
        l = 0
        for i in range(len(s)):
            if s[i] in char_map:
                l = max(char_map[s[i]]+1, l)
            char_map[s[i]] = i
            res = max(res, i-l+1)
        return res            

                
