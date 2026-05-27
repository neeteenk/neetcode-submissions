class Solution:
    def trap(self, height: List[int]) -> int:
        # TC: O(N^2)
        if not height:
            return 0

        n = len(height)
        res = 0
        for i in range(n):
            leftMax = rightMax = height[i]
            for j in range(i):
                leftMax = max(leftMax, height[j])
            
            for k in range(i+1, n):
                rightMax = max(rightMax, height[k])

            res += min(leftMax, rightMax) - height[i]
        
        return res