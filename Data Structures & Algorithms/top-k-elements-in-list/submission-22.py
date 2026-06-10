class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        fre = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for n, c in count.items():
            fre[c].append(n)

        res = []
        for i in range(len(fre)-1, 0, -1):
            for num in fre[i]:
                res.append(num)
                if len(res) == k:
                    return res
