class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n  # What do we need?
            if diff in prevMap:  # Have we seen it?
                return [prevMap[diff], i]
            prevMap[n] = i  # Remember this number for later