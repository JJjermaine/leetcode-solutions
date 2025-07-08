class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # method based off immediate intuition
        # traverse from king to seek rooks in all directions

        # find king position
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "R":
                    king_row = row
                    king_col = col
            
        count = 0
        # traverse from king position to right of board
        for i in range(king_col, len(board)):
            if board[king_row][i] == "p":
                count += 1
                break
            elif board[king_row][i] == "B":
                break

        # traverse from king position to left of board
        for i in range(king_col -1, -1, -1):
            if board[king_row][i] == "p":
                count += 1
                break
            elif board[king_row][i] == "B":
                break

        # traverse from king position to bottom of board
        for i in range(king_row, len(board)):
            if board[i][king_col] == "p":
                count += 1
                break
            elif board[i][king_col] == "B":
                break

        # traverse from king position to top of board
        for i in range(king_row -1, -1, -1):
            if board[i][king_col] == "p":
                count += 1
                break
            elif board[i][king_col] == "B":
                break

        return count
            
            
        