class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # greedy stack
        # observations:
        # simulate taking ab's then ba's
        # then simulate taking ba's then ab's

        stack = []
        temp = []
        first = 0
        second = 0

        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2] == "a" and stack[-1] == "b":
                stack.pop()
                stack.pop()
                first += x

        for i in range(len(stack)):
            temp.append(stack[i])
            if len(temp) >= 2 and temp[-2] == "b" and temp[-1] == "a":
                temp.pop()
                temp.pop()
                first += y

        stack = []
        temp = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2] == "b" and stack[-1] == "a":
                stack.pop()
                stack.pop()
                second += y

        for i in range(len(stack)):
            temp.append(stack[i])
            if len(temp) >= 2 and temp[-2] == "a" and temp[-1] == "b":
                temp.pop()
                temp.pop()
                second += x

        return max(first, second)
        
