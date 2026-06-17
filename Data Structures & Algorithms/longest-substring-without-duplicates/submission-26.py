class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char_map = set()
        l = 0
        for i in range(len(s)):
            while s[i] in char_map:
                char_map.remove(s[l])
                l += 1
            char_map.add(s[i])
            res = max(res, i-l+1)
        return res            

                
