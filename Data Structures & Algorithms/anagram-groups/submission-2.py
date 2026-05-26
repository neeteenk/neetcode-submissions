class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   
        # sorted("eat") -> ["a", "e", "t"]
        # join() combines list elements into a single string.
        # TC: O(n * (k logk) (sorted)) | SC: O(n*k)
        ans = []
        mpp = {}
        for x in strs:
            current = "".join(sorted(x))
            if current in mpp:
                ans[mpp[current]].append(x)
            else:
                ans.append([x])
                mpp[current] = len(ans) - 1
        return ans