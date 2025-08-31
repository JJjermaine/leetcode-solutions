class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs
        def dfs(row, col, remaining, temp):
            if remaining == "":
                return True
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            temp.add((row, col))
            for x, y in directions:
                new_row = row + x
                new_col = col + y
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in temp:
                    if board[new_row][new_col] == remaining[0]:
                        if dfs(new_row, new_col, remaining[1:], temp):
                            return True
            temp.remove((row, col))
            return False

        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:

                    if dfs(i, j, word[1:], set((i, j))):
                        return True
        return False