# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         l = 0
#         r = 1
#         ans = "a"*10001
#         while r < len(s):
#             if not t or not s:
#                 return ""
#             strings = list(t)
#             while s[l] not in strings:
#                 l += 1
#                 continue
#             r = l+1
#             while len(strings) != 0:
#                 if s[r] in strings:
#                     strings.remove(s[r])
#                 r += 1
#             current = s[l:r+1]
#             if len(ans) > len(current):
#                 ans = s[l:r+1]

#         if ans == "a"*10001: return ""
#         else: return ans

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
            


                

                











        