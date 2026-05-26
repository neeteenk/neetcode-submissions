class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        seen = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in seen:
                ans.append([str])
                seen[sorted_str] = len(ans)-1
            else:
                ans[seen[sorted_str]].append(str)
        
        return ans
