class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for c in s:
            if c.isalnum():
                newstr += c.lower()
        l, r = 0, len(newstr) -1
        while l < r:
            if newstr[l] != newstr[r]:
                return False
            l += 1
            r -= 1

        return True



        