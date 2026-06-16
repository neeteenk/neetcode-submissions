from collections import defaultdict
class Solution:
    # TC: o(n*m)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        for x in s1:
            count[x]+=1
        
        x = len(s1)
        r = x - 1
        l = 0
        while r < len(s2):
            count2 = defaultdict(int)
            for i in range(x):
                count2[s2[i+l]]+=1
            if count == count2:
                return True
            l+=1
            r+=1
        return False
