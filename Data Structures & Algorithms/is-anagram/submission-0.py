from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = jar, t = raj -> True
        # s = jar, t = jam -> False
        # s = racecar, t = carrace -> True
        # return sorted(s) == sorted(t)
        return Counter(s) == Counter(t)
        