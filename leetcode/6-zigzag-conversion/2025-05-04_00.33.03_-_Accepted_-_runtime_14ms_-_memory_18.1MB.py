class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # associate it with the row and sort and read off by row
        if numRows == 1:
            return s
        n = len(s)
        zig = defaultdict(str)
        num = 1
        increment = True
        decrement = False
        for i in range(n):
            zig[num] += s[i]

            if increment:
                num += 1
            else:
                num -= 1

            if num == numRows and increment:
                increment = False
            if num == 1 and not increment:
                increment = True

        res = ""
        for k, v in zig.items():
            res += v
        return res

            

        