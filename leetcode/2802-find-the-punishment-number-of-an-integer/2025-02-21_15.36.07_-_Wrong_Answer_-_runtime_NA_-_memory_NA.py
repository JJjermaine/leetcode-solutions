class Solution:
    def punishmentNumber(self, n: int) -> int:
        self.res = 0

        # 1296
        # split into 1 296, 1 2 96, 1 2 9 6, 12 9 6, 12 96, 129 6
        def split(i):
            numstr = str(i*i)
            partition = []
            # split into all possible ways
            def backtracking(ind, path):
                if ind == len(numstr):
                    partition.append(" ".join(path))
                    return

                for i in range(ind, len(numstr)):
                    backtracking(i+1, path + [numstr[ind:i+1]])

            backtracking(0, [])

            # combine in all possible ways
            for string in partition:
                arr = list(map(int, string.split()))
                curr = 0
                for num in arr:
                    curr += num
                if curr == i:
                    self.res += (i * i)
            

        for i in range(n+1):
            split(i)

        return self.res
            
        