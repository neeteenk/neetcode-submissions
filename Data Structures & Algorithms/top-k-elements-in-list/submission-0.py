class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TC: NlogK | SC:(N+K)
        mpp = dict()
        for num in nums:
            mpp[num] = 1 + mpp.get(num, 0)

        heap = [] #minheap
        for num in mpp.keys():
            heapq.heappush(heap, (mpp[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

