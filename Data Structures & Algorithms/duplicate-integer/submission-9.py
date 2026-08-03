class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for _, x in enumerate(nums):
            if x in seen:
                return True
            else:
                seen[x] = x
        return False