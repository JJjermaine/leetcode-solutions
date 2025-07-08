class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        pointer = 0
        for i in range(len(s)):
            stack.append(s[i])
            if "".join(stack[len(stack)-len(part):]) == part and len(stack) >= len(part):
                for j in range(len(part)):
                    stack.pop()
            
        return "".join(stack)