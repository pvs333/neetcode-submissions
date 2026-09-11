class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        l = 0
        r = 1
        m = 0
        while r < len(s):
            if s[r] in s[l:r]:
                m = max(m, r-l)
                l+=1
                continue
            r+=1
        m = max(m,r-l)
        return m