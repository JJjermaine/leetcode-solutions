class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False]*cols for _ in range(rows)]

        def dfs(row, col, parent_row, parent_col, char, depth):
            if visited[row][col]:
                return depth >= 4  # found a cycle if depth >= 4 and revisiting

            visited[row][col] = True
            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if (new_row, new_col) == (parent_row, parent_col):
                        continue  # don't go back to parent
                    if grid[new_row][new_col] == char:
                        if dfs(new_row, new_col, row, col, char, depth + 1):
                            return True

            return False

        found_cycle = False
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j], 1):
                        found_cycle = True
                        break
            if found_cycle:
                return True
        return False