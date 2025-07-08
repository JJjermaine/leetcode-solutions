class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = set()
        res = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in count: 
                    res.append(grid[i][j]) # add repeating number
                count.add(grid[i][j])

        for i in range(1, len(grid) * len(grid) + 1):
            if i not in count:
                res.append(i) # add missing number

        return res

        


        