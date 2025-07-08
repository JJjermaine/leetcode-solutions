class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # intuition: if repeating the moves 2 or 4 times doesn

        directions = [1, 0, 0, 0] # N, W, S, E
        location = [0, 0] # vertical, horizontal

        for i in range(4):
            for move in instructions:
                if move == "G":
                    if directions == [1, 0, 0, 0]:
                        location[0] += 1
                    if directions == [0, 1, 0, 0]:
                        location[1] += 1
                    if directions == [0, 0, 1, 0]:
                        location[0] -= 1
                    if directions == [0, 0, 0, 1]:
                        location[1] -= 1

                if move == "L": # shift left
                    directions = directions[1:] + directions[:1]

                if move == "R": # shift right
                    directions = directions[-1:] + directions[:-1]

        
        if location == [0, 0]:
            return True
        return False