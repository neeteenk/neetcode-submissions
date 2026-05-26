class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        seen = set(nums)
        maxLen = 0
        
        for x in nums:
            cnt = 0
            while x + 1 in seen:
                cnt+=1
                x+=1
            maxLen = max(cnt, maxLen)
        return maxLen + 1