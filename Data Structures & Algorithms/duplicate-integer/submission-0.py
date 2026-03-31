class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        for num in nums:
            # if my_map does not have num in it then add num to my_map
            if my_map.get(num) == None:
                my_map[num] = num
            else:
                return True

        return False