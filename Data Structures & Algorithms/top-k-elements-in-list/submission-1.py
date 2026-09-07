class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        fr = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n,0)+1
        
        for n, c in count.items():
            fr[c].append(n)

        res = []

        for i in range(len(fr)-1, 0, -1):
            for n in fr[i]:
                res.append(n)
                if len(res) == k:
                    return res