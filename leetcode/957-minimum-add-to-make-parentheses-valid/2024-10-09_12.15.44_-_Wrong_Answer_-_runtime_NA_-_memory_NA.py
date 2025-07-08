class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        close = 0
        open = 0

        for char in s:
            if char == "(":
                open += 1
            
            elif char == ")":
                close += 1

        return (abs(open - close))
