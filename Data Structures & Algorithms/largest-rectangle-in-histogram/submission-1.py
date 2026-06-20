class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # TLDR; ans[i] x (nse - pse - 1)
        # st.top() = index of the bar that stops you.
        # You cannot stand on the obstacle.
        # So start from the next position.    
        # we do atlast +1, -1 in leftMost and rightmost, as we need to take values before obstacle
        # a bar  of height[6] cant settle for height of bar 5 or height bar 7
        # https://takeuforward.org/data-structure/area-of-largest-rectangle-in-histogram
        # TC: O(n)
        # SC: O(n)

        n = len(heights)
        stack = []
        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)


        stack = []
        rightMost = [n] * n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        maxArea = 0
        for i in range(n):
            leftMost[i]+=1
            rightMost[i]-=1
            maxArea = max(maxArea, heights[i] * (rightMost[i] -  leftMost[i] + 1))
        return maxArea