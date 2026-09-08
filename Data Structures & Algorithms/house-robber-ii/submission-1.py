class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        dp1 = [0]* (len(nums)-1)
        dp2 = [0]* (len(nums)-1)

        dp1[0] = nums[0]
        dp2[0] = nums[1]
        
        for i in range(1, len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i+1])
        
        print(dp1)
        print(dp2)
        return max(max(dp1),max(dp2))