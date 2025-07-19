class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            # if we encounter ), then reverse until ( is seen
            if s[i] == ")":
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop() # pop the (
                temp = temp[::-1]
                while temp:
                    stack.append(temp.pop())
                
            else:
                stack.append(s[i])
        return "".join(stack)