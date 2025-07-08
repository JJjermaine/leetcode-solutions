class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # To track indices of unmatched '('
        to_remove = set()  # To store indices of parentheses to remove
        
        # First pass: Identify unmatched '(' and ')'
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Track index of '('
            elif char == ')':
                if stack:
                    stack.pop()  # Match with a '('
                else:
                    to_remove.add(i)  # Unmatched ')'
        
        # Add remaining unmatched '(' to the set
        to_remove.update(stack)
        
        # Second pass: Build the result string
        res = []
        for i, char in enumerate(s):
            if i not in to_remove:
                res.append(char)
        
        return ''.join(res)