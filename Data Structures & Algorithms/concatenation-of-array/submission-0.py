class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        totalLen = 2 * n
        ans = []
        for i in range(totalLen):
            ans.append(nums[i%n])
        return ans
