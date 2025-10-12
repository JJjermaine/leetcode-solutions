class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # xy is the length of grid * length of grid[0]
        # zx is largest in each grid[i]
        # yz is largest x in each grid[x][i]

        zeroes = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zeroes += 1

        xy = len(grid) * len(grid[0]) - zeroes
            

        zx = 0
        for i in range(len(grid)):
            zx += max(grid[i])

        yz = 0
        for i in range(len(grid[0])):
            largest = 0
            for j in range(len(grid)):
                largest = max(largest, grid[j][i])
            
            yz += largest
        return xy + zx + yz