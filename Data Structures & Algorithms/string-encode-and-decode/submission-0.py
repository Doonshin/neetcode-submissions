class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}:{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # 「長さ」の部分を読む（:まで）
            j = i
            while s[j] != ':':
                j += 1
            length = int(s[i:j])
            # j+1 から j+1+length までが文字列本体
            res.append(s[j+1:j+1+length])
            # 次の文字列へ進む
            i = j + 1 + length
        return res
