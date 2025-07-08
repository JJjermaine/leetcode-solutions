class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        # get index with most amount of 1's
        count = {}
        for i in range(len(grid)):
            wins = 0
            for j in range(len(grid)):
                wins += (grid[i][j])

            count[i] = wins

        return max(count, key=count.get)

                
        