class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #TC: O(n) | SC: O(n)
        mpp = {}
        for i in range(len(nums)):
            remTarget = target - nums[i]
            if remTarget in mpp:
                return [mpp[remTarget], i]
            mpp[nums[i]] = i
        return []