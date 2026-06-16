class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(N^2)
        n = len(prices)
        ans = -1
        for i in range(n):
            for j in range(i+1):
                ans = max(ans, prices[i] - prices[j])
        return ans