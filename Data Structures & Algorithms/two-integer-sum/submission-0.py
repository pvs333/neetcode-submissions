class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, x in enumerate(nums):
            d = target - x
            if d in map:
                return [map[d], i]
            map[x] = i
        return []