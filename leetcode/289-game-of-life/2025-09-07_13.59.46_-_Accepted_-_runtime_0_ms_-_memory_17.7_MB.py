class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1 -> 0 if < 2 neighbors == 0
        # 1 -> 1 if 2 or 3 neighbors == 1
        # 1 -> 0 if > 3 neighbors == 0
        # 0 -> 1 if exactly 3 neighbors == 0
        # help from gpt
        rows, cols = len(board), len(board[0])
        directions = [
            (0,1),(0,-1),(1,0),(-1,0),
            (1,1),(1,-1),(-1,1),(-1,-1)
        ]

        def live_neighbors(r: int, c: int) -> int:
            cnt = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Count neighbors that were alive in the original state:
                    # 1 (live) or 2 (live->dead). Do NOT count -1.
                    if board[nr][nc] > 0:  # 1 or 2
                        cnt += 1
            return cnt

        # First pass: mark transitions
        for i in range(rows):
            for j in range(cols):
                ln = live_neighbors(i, j)
                if board[i][j] == 1:
                    if ln < 2 or ln > 3:
                        board[i][j] = 2         # live -> dead
                else:  # board[i][j] == 0
                    if ln == 3:
                        board[i][j] = -1        # dead -> live

        # Second pass: finalize to 0/1
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
        