class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for c in s:
            if c.isdigit():
                stack.pop()
            else:
                stack.append(c)

        res = ""
        for c in stack:
            res += c

        return res

        