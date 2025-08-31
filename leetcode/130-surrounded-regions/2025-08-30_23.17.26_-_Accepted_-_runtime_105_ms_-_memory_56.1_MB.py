class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # unless its connected to a corner, its guaranteed to be captured
        rows = len(board)
        cols = len(board[0])
        seen = set()

        def dfs(row, col):
            edge = False
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            if row == 0 or row == rows-1:
                edge = True
            if col == 0 or col == cols-1:
                edge = True
            
            temp.add((row, col))
            seen.add((row, col)) 
            for x, y in directions:
                new_row = row + x
                new_col = col + y
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in temp:
                    if board[new_row][new_col] == "O":
                        edge = dfs(new_row, new_col) or edge
            return edge

            


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in seen:
                    temp = set()
                    edge = dfs(i, j)

                    if not edge: # it touched no edge so made every O into an X
                        for x, y in temp:
                            board[x][y] = "X"

                 