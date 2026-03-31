class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res 
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res

if __name__ == "__main__":
    sol = Solution()
    strr = ["Hello", "World"]
    encoded_sol = sol.encode(strr)
    decoded_sol = sol.decode(encoded_sol)