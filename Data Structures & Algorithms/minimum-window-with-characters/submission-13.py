

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        l = 0
        res = [-1, -1]
        resLen = float("inf")  
        have, need = 0, len(countT)

        for i in t:
            countT[i] = 1 + countT.get(i, 0)

        have, need = 0, len(countT)

        for r in range(len(s)):
            c = s[r]
            if c in countT:
                window[c] = 1 + window.get(c, 0)
                if window[c] == countT[c]:
                    have += 1
            while have == need:
                if resLen > (r - l + 1):
                    resLen = r - l + 1
                    res = [l, r]
                if s[l] in countT:
                    window[s[l]] = window.get(s[l]) - 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
                



        