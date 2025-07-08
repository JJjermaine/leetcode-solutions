class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # needed a little help
        rows = len(land)
        cols = len(land[0])
        visited = set()

        def dfs(row, col, bounds):
            if (row, col) in visited:
                return
            bounds[0] = min(bounds[0], row)
            bounds[1] = min(bounds[1], col)
            bounds[2] = max(bounds[2], row)
            bounds[3] = max(bounds[3], col)  
            visited.add((row, col))
            direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for d in direction:
                dx, dy = d
                new_row = row + dx
                new_col = col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if land[new_row][new_col] == 1:
                        dfs(new_row, new_col, bounds)

        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and land[i][j] == 1:
                    bounds = [rows, cols, 0, 0]
                    dfs(i, j, bounds)
                    res.append(bounds)
        return res