class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(heights)-1
        largest_water = 0
        for i in range(len(heights)):
            l = 0
            for j in range(len(heights) - i):
                while l < r:
                    dist = r - l
                    lowest_point = min(heights[l], heights[r])

                    current_water = lowest_point * dist 

                    largest_water = max(current_water, largest_water)
                    l += 1

            r -= 1

        return largest_water