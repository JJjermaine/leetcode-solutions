class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors.extend(color for color in colors.copy())
        count = 0
        for i in range(1, len(colors)//2+1):
            if colors[i-1] != colors[i] and colors[i] != colors[i+1]:
                count += 1

        return count
        