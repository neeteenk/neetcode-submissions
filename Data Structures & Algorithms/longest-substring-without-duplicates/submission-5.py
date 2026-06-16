class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TC : O(n) | SC: O(m)
        l, r, ans = 0, 0, 0
        seen = set()

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            ans = max(ans, r - l + 1)
            r += 1

        return ans