class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        res = []
        num = 1

        for char in pattern + "I":
            stack.append(str(num))
            num += 1
            if char == "I":
                while stack:
                    res.append(stack.pop())
        return "".join(res)
        