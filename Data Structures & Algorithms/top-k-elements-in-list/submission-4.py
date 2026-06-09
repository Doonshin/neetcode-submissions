class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        out = []
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for i in range(k):
            out.append(max(count, key=count.get))
            count.pop(max(count, key=count.get))
        return out

