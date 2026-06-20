class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n-1, -1, -1): #did mistake here (start, stop, sep)
            while st and temperatures[st[-1]]<=temperatures[i]:
                st.pop()
            ans[i] = st[-1] - i if st else 0
            st.append(i)
        return ans
