from typing import List
import math

class Solution:
    """
     Binary search the cut in the smaller array until the largest element on 
     the left half is ≤ the smallest element on the right half (`left1 ≤ right2` and `left2 ≤ right1`), 
     then the median lies at the partition boundary.
     TC: O(log(min(n1, n2)))

           LEFT HALF      |      RIGHT HALF

            nums1  ... left1      |      right1 ...
            nums2  ... left2      |      right2 ...

            Need:

            left1 <= right2
            left2 <= right1
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1, n2 = len(nums1), len(nums2)
        lo, hi = 0, n1

        while lo<=hi:
            cut1 = lo + (hi - lo)//2
            cut2 =  (n1 + n2 + 1)//2 - cut1
            left1 = -math.inf if cut1 == 0 else nums1[cut1-1]
            left2 = -math.inf if cut2 == 0 else nums2[cut2-1]
            
            right1 = math.inf if cut1 == n1 else nums1[cut1]
            right2 = math.inf if cut2 == n2 else nums2[cut2]

            if left1<=right2 and left2<=right1:
                if (n1 + n2)%2 == 0:
                    return (max(left1, left2) + min(right1, right2))/2.0
                else:
                    return float(max(left1, left2))
            elif left1 > right2:
                hi = cut1 - 1
            else:
                lo = cut1 + 1
        return 0.0


