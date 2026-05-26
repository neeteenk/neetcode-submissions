class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n - 1
            remTarget = 0 - nums[i]
            while j < k:
                if nums[j] + nums[k] == remTarget:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]: 
                        j+=1
                    
                    while j < k and nums[k-1] == nums[k]: 
                        k-=1
                    
                    j+=1
                    k-=1
                elif nums[j] + nums[k] > remTarget:
                    k-=1
                else:
                    j+=1  
        return ans