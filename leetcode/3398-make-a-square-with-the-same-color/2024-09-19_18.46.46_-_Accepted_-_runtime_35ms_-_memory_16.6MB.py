class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        # for every 2x2 square, check if at least 3 whites or at least 3 blacks

        for row in range(len(grid)-1):
            for col in range(len(grid)-1):
                white = 0
                black = 0
                if grid[row][col] == "W": white += 1
                else: black += 1

                if grid[row+1][col] == "W": white += 1
                else: black += 1

                if grid[row][col+1] == "W": white += 1
                else: black += 1

                if grid[row+1][col+1] == "W": white += 1
                else: black += 1
            
                if white >= 3 or black >= 3:
                    return True
        return False

        