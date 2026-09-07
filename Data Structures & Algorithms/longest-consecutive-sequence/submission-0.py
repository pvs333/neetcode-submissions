class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        lC = 0

        for n in nums:
            if(n-1) not in s:
                l = 0
                while(n+l) in s:
                    l+=1
                lC = max(lC, l)
        
        return lC