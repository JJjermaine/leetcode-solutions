class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest_water = 0
        l = 0
        r = len(height) - 1

        while l < r:
            dist = r - l
            lowest_point = min(height[l], height[r])
            current_water = lowest_point * dist

            largest_water = max(current_water, largest_water)

            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1

        return largest_water
            