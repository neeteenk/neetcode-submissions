class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        seen = [0] * 26
        for i in range(len(s)):
            ch1 = ord(s[i]) - ord('a')
            ch2 = ord(t[i]) - ord('a')
            seen[ch1]+=1
            seen[ch2]-=1

        for x in seen:
            print(x)
            if x > 0:
                return False
        return True
