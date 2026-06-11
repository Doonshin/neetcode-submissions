


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        #mapping appeared number and the frequency

        # using heap, keeping the highest number untill k
        # extract them and store in list using loop

        heap = []
        for num, fre in count.items():
            heapq.heappush(heap, (fre, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        