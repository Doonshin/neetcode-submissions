class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        size = []
        st = ""
        for s in strs:
            size.append(len(s))
        for sz in size:
            st += str(sz)
            st += ','
        st += '!'
        for s in strs:
            st += s
        return st

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        size, res, i = [], [], 0  
        while s[i] != '!':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            size.append(int(cur))
            i += 1
        i += 1
        for sz in size:
            res.append(s[i: i + sz])
            i += sz
        return res


