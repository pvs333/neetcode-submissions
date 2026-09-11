class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i, x in enumerate(numbers):
            d = target - x
            if d in map:
                return [map[d]+1, i+1]
            map[x] = i
        return []
            