from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()

        have = 0
        required = len(need)

        l = 0
        res = ""
        res_len = float("inf")

        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                # Current window is valid
                if r - l + 1 < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1

                # Remove left character
                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                l += 1

        return res