class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # associate it with the row and sort and read off by row
        if numRows == 1:
            return s
        n = len(s)
        zig = []
        num = 1
        increment = True
        decrement = False
        for i in range(n):
            zig.append((num, s[i]))

            if increment:
                num += 1
            else:
                num -= 1

            if num == numRows and increment:
                increment = False
            if num == 1 and not increment:
                increment = True

        res = []
        for i in range(1, numRows+1):
            for j in range(n):
                if zig[j][0] == i:
                    res.append(zig[j][1])
        return "".join(res)

            

        