class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # copied from sol
        def isValid(s):
            stack = []
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append((i, "("))
                elif s[i] == ")":
                    if stack and stack[-1][1] == "(":
                        stack.pop()
                    else:
                        stack.append((i, ")"))
            return len(stack) == 0, stack

        def dfs(s, left, right):
            nonlocal res
            visited.add(s)
            if left == 0 and right == 0 and isValid(s)[0]:
                res.add(s)   # use a set

            for i, char in enumerate(s):
                if char.isalpha():
                    continue
                if (char == "(" and left == 0) or (char == ")" and right == 0):
                    continue

                new = s[:i] + s[i+1:]
                if new not in visited:
                    if char == "(":
                        dfs(new, left - 1, right)
                    elif char == ")":
                        dfs(new, left, right - 1)

        stack = isValid(s)[1]
        lc = sum(1 for val in stack if val[1] == "(")
        rc = len(stack) - lc

        res = set()
        visited = set()
        dfs(s, lc, rc)
        return list(res)
