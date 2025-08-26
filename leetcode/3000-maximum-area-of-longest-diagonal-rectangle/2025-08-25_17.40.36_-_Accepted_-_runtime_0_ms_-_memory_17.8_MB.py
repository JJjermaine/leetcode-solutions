class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        largest_area = 0
        largest_diag = 0
        for length, width in dimensions:
            diag = sqrt((length * length) + (width * width))
            area = length * width
            if diag >= largest_diag:
                if diag == largest_diag:
                    largest_area = max(area, largest_area)
                else:
                    largest_area = area
                largest_diag = diag

        return largest_area