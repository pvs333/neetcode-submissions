class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mS = nums[0]
        cS = 0

        for n in nums:
            cS = max(cS,0) + n
            mS = max(mS, cS)

        return mS