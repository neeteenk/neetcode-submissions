class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(nlogn) | O(n)
        count = defaultdict(int)
        for n in nums:
            count[n]+=1
        
        arr = []
        for x, cnt in count.items():
            arr.append([cnt, x])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res