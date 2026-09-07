class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = defaultdict(list)

        for s in strs:
            c = [0] * 26
            for j in s:
                c[ord(j) - ord("a")] += 1
            r[tuple(c)].append(s)
        
        return list(r.values())