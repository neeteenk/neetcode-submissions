class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge -> return median
        # o(m+n)
        nums3 = []
        for x in nums1:
            nums3.append(x)
        
        for y in nums2:
            nums3.append(y)

        nums3.sort()
        nums3len = len(nums3)
        mid = nums3len//2
        
        if nums3len%2 == 0:
            return (nums3[mid] + nums3[mid-1])/2
        else:
            return nums3[mid]
