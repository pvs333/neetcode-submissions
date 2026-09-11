class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26
        a = ord('a')

        for c in s1:
            need[ord(c) - a] += 1

        for c in s2[:len(s1)]:
            window[ord(c) - a] += 1

        if window == need:
            return True

        for i in range(len(s1), len(s2)):
            window[ord(s2[i]) - a] += 1
            window[ord(s2[i - len(s1)]) - a] -= 1
            if window == need:
                return True

        return False