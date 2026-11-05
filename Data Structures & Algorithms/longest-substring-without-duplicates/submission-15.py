class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l, res = 0, 0

        for r in range(len(s)):
            if s[r] in mp:
                # move left pointer
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            res = max((r - l + 1), res)
        
        return res
