class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical = 0
        horizontal = 0
        for move in moves:
            if move == "U":
                vertical += 1
            if move == "D":
                vertical -= 1
            if move == "R":
                horizontal += 1
            if move == "L":
                horizontal -= 1

        return (vertical == 0 and horizontal == 0)
        