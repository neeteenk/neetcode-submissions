class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # TC: O(nlogn + mlogm) | SC: O(1)
        if len(s)!=len(t):
            return False
        
        return sorted(s) == sorted(t)