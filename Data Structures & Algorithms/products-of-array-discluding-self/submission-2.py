class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TC : O(n) | SC : O(n)
        n = len(nums)
        pref = [0] * n
        suffix = [0] * n
        res = [0] * n

        pref[0] = suffix[n-1] = 1
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = pref[i] * suffix[i]
        return res