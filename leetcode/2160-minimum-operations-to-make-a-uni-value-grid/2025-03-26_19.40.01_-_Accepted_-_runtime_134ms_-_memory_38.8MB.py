class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        mod = grid[0][0] % x
        rows = len(grid)
        cols = len(grid[0])

        res = 0
        arr = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] % x != mod:
                    return -1
                arr.append(grid[i][j])
        
        arr.sort()
        middle = arr[len(arr)//2]
        for num in arr:
            if num == middle:
                continue
            res += abs((num-middle) // x)
        return res




        