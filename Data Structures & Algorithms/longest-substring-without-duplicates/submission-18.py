class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char_dic = {}
        l = 0
        for i, c in enumerate(s):
            if c in char_dic:
                l = max(l, char_dic[c] + 1)#注意　l = char_dic[c] + 1ではない。lより前の数字は無視する
            char_dic[c] = i 
            res = max(i-l+1, res) #要素数は＋１インデックスの差はそのままひく
        return res