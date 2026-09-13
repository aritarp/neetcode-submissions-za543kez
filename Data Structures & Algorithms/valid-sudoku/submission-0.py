class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set() # using HashSet

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                digit = board[r][c]
                if (
                    (r,digit) in seen or
                    (digit, c) in seen or
                    (r // 3, c // 3, digit) in seen
                ):
                    return False
                
                seen.add((r,digit))
                seen.add((digit,c))
                seen.add((r//3,c//3,digit))

        return True