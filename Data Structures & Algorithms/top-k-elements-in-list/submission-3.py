from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        appearance_tracker = Counter(nums)
        sorted_keys = sorted(appearance_tracker, key=lambda x: appearance_tracker[x], reverse = True)
        return sorted_keys[:k]