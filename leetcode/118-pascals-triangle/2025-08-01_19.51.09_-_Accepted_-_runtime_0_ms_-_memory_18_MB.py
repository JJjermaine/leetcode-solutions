class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[] for _ in range(numRows)]

        for i in range(numRows):
            for j in range(i+1):
                # get the 2 above
                if i> 1 and j > 0 and j < i:
                    res[i].append(res[i-1][j-1] + res[i-1][j])
                else:
                    res[i].append(1)
        
        return res