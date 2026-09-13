class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None or s == "":
            return True

        s = ''.join(char for char in s.lower() if char.isalnum())
        char_list = list(s)
        reversed_list = char_list[::-1]
        reversed_str = ''.join(reversed_list)

        if s == reversed_str:
            return True
        return False