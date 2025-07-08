class Solution:
    def finalString(self, s: str) -> str:
        stack = []
        i_count = 0
        for char in s:
            if char == "i":
                stack = stack[::-1]
            else:
                stack.append(char)

        
        return ''.join(stack)
