class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # // for integer divison
        nums.sort()
        n = len(nums)
        lo, hi = 0, n-1
        
        while lo<=hi:
            mid = lo + (hi - lo)//2;
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
