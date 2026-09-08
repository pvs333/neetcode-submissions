class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxL = [0] * len(nums)
        minL = [0] * len(nums)

        maxL[0] = nums[0]
        minL[0] = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            maxL[i] = max(n, maxL[i-1]*n, minL[i-1]*n)
            minL[i] = min(n, maxL[i-1]*n, minL[i-1]*n)

        return max(maxL)