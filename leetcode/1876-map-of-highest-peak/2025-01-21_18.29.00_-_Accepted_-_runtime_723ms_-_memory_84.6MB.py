class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        #two pass
        rows = len(isWater)
        cols = len(isWater[0])
        height = [[float('inf')] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if isWater[row][col] == 1:
                    height[row][col] = 0
                else:
                    if row > 0:
                        height[row][col] = min(height[row][col], height[row-1][col] + 1)
                    if col > 0:
                        height[row][col] = min(height[row][col], height[row][col-1] + 1)

        for row in range(rows-1,-1,-1):
            for col in range(cols-1,-1,-1):
                if row < rows - 1:
                    height[row][col] = min(height[row][col], height[row+1][col] + 1)
                if col < cols - 1:
                    height[row][col] = min(height[row][col], height[row][col+1] + 1)

        return height
