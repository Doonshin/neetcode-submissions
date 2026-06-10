


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_fre = {}
        bucket = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            top_fre[n] = top_fre.get(n, 0) + 1
        for num, count in top_fre.items():
            bucket[count].append(num)
            
        res = []
        l = len(nums)
        while len(res) < k:
            for num in bucket[l]:
                res.append(num)

                if len(res) == k:
                    return res
            l -= 1

        return res