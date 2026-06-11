class Solution:
    # / floating point division
    # // floar division
    def canFinishPile(self, k: int, piles: List[int], h: int) -> bool:
        totalHrs = 0
        for pile in piles:
            totalHrs+=(pile+k-1)//k
        
        return totalHrs <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            mid = l + (r - l) // 2
            if self.canFinishPile(mid, piles, h):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans