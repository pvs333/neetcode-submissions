class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        pos = []
        out = [0] * len(nums)

        pre.append(nums[0])
        pos.append(nums[len(nums)-1])

        for i in range(1, len(nums)):
            pre.append(pre[i-1] * nums[i])
            pos.append(pos[i-1] * nums[-1-i])

        pos.reverse()
        
        out[0] = pos[1]
        out[len(nums)-1] = pre[-2]

        for i in range(1, len(nums)-1):
            out[i] = pre[i-1]*pos[i+1]

        return out