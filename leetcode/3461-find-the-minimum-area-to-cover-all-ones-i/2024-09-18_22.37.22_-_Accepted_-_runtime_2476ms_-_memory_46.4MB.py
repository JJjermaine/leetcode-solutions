class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # my approach based off immediate intuition
        # traverse from left to right, right to left, top to bottom, bottom to top
        # whenever we see a 1, mark the location. This will give us all the bounds
        # finally, get the distance between all the bounds to compute the area

        rows = len(grid)
        cols = len(grid[0]) 

        left_bound = 0
        right_bound = 0
        top_bound = 0
        bottom_bound = 0

        found = False

        # scan left to right
        for col in range(cols):
            for row in range(rows):
                if grid[row][col] == 1:
                    left_bound = col
                    found = True

            if found: break

        found = False

        # scan right to left
        for col in range(cols -1, -1, -1):
            for row in range(rows):
                if grid[row][col] == 1:
                    right_bound = col + 1
                    found = True
            
            if found: break

        found = False

        # scan top to bot
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    top_bound = row
                    found = True

            if found: break

        found = False

        # scan bot to top
        for row in range(rows -1, -1, -1):
            for col in range(cols):
                if grid[row][col] == 1:
                    bottom_bound = row + 1
                    found = True

            if found: break

        length = right_bound - left_bound
        height = bottom_bound - top_bound

        return length * height


        