class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i, j = 0, 0
        n = len(nums)
        ans = [1] * n
        for i in range(len(nums)):
            left, right = 0, i+1
            while left < i:
                ans[i]*=nums[left]
                left+=1
            
            while right < n:
                ans[i]*=nums[right]
                right+=1
        
        return ans