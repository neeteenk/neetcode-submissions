class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): 
            return False
        
        dict_s = dict()
        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1
        
        for ch in t:
            if ch not in dict_s:
                return False
            dict_s[ch]-=1
            if dict_s[ch] == 0:
                del dict_s[ch]
        return True