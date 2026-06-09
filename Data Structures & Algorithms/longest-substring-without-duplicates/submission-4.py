class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = []
        res = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.append(s[r])
            res = max(res, r - l + 1)
        return res



    
