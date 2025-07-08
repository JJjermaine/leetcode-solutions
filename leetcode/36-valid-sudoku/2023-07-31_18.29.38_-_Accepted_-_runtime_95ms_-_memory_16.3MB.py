class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            map = {}
            for num in row:
                if num != '.':
                    if map.get(num):
                        return False
                    map[num] = 1

        for col in range(9):
            map = {}
            for row in range(9):
                num = board[row][col]
                if num != '.':
                    if map.get(num):
                        return False
                    map[num] = 1

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                map = {}
                for k in range(3):
                    for l in range(3):
                        num = board[i + k][j + l]
                        if num != '.':
                            if map.get(num):
                                return False
                            map[num] = 1

        return True