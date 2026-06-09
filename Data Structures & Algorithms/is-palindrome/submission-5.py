class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join(c.lower() for c in s if c.isalnum())

        for i in range(len(res) // 2):
            if res[i] != res[-(i+1)]:
                return False
        return True
