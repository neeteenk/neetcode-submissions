class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   
        # defaultdict
        # If key does not exist, create an empty list automatically.
        # Lists cannot be hashmap keys. So convert to immutable tuple.
        mpp = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')]+=1
            mpp[tuple(count)].append(s)
        return list(mpp.values())
