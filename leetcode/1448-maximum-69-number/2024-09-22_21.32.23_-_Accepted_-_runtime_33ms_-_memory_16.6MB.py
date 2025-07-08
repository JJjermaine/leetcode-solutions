class Solution:
    def maximum69Number (self, num: int) -> int:
        string = str(num)
        changed = False
        stack = []
        for char in string:
            if char == "6" and changed == False:
                stack.append("9")
                changed = True
            else:
                stack.append(char)

        res = ''.join(stack)
        return int(res)

        return int(string)

        