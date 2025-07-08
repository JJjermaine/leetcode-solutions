class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return n * m

        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(len(ops)):
            
            x, y = ops[i][0], ops[i][1]
        
            for i in range(x):
                for j in range(y):
                    matrix[i][j] += 1

        count = {}

        for i in range(m):
            for j in range(n):
                if matrix[i][j] not in count:
                    count[matrix[i][j]] = 1
                else:
                    count[matrix[i][j]] += 1

        if count:
            max_key = max(count.keys())
            max_value = count[max_key]

        return max_value
        