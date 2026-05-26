class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   
        # defaultdict
        # If key does not exist, create an empty list automatically.
        mpp = defaultdict(list)
        for s in strs:
            sortedStr = "".join(sorted(s))
            mpp[sortedStr].append(s)
        return list(mpp.values())