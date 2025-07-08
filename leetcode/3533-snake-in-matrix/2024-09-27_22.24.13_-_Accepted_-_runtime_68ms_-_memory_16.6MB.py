class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        horizontal = 0
        vertical = 0
        grid = [[j + i * n for j in range(n)] for i in range(n)] # create grid
        for command in commands:
            if command == "RIGHT":
                horizontal += 1
            
            if command == "LEFT":
                horizontal -= 1

            if command == "UP":
                vertical -= 1

            if command == "DOWN": # add 1 for down because relative to position from zero
                vertical += 1

        return grid[vertical][horizontal]

        