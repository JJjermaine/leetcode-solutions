class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # keep going right until the end, then down, then left, then up, then right....
        res = []
        visited = set()
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = 0
        right = True
        down = False
        left = False
        up = False

        while len(res) < rows * cols:
            if right:
                res.append(matrix[i][j])
                visited.add((i, j))
                if not 0 <= j+1 < cols or (i, j+1) in visited:
                    down = True
                    right = False
                    i += 1
                    continue
                j += 1
            elif down:
                res.append(matrix[i][j])
                visited.add((i, j))
                if not 0 <= i+1 < rows or (i+1, j) in visited:
                    left = True
                    down = False
                    j -= 1
                    continue
                i += 1
            elif left:
                res.append(matrix[i][j])
                visited.add((i, j))
                if not 0 <= j-1 < cols or (i, j-1) in visited:
                    up = True
                    left = False
                    i -= 1
                    continue
                j -= 1
            elif up:
                res.append(matrix[i][j])
                visited.add((i, j))
                if not 0 <= i-1 < rows or (i-1, j) in visited:
                    right = True
                    up = False
                    j += 1
                    continue
                i -= 1
        return res
