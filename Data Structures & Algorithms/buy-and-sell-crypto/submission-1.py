import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(N)
        n = len(prices)
        minPrice = math.inf
        ans = -1
        for i in range(n):
            minPrice = min(minPrice, prices[i])
            ans = max(prices[i] - minPrice, ans)

        return ans