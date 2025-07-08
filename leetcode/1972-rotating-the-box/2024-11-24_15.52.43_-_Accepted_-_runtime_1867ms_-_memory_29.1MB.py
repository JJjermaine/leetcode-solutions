class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])
        rotate = [['.'] * rows for _ in range(cols)]

        for i, row in enumerate(box):
            bottom = cols - 1
            for j in range(cols - 1, -1, -1):
                if row[j] == "#":
                    rotate[bottom][rows-1-i] = "#" 
                    bottom -= 1
                elif row[j] == '*':
                    rotate[j][rows - 1 - i] = "*"
                    bottom = j - 1
        return rotate
        