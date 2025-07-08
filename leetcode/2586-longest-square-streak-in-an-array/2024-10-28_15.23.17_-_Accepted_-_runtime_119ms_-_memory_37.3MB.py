import math
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # dp, increase value in dic if the sqrt is already in dic
        nums.sort()
        count = {}

        max_streak = 0
        for num in nums:
            root = math.isqrt(num)
            if root * root == num and root in count:
                count[num] = count[root] + 1
            else:
                count[num] = 1

        max_streak = max(count.values())
        return max_streak if max_streak > 1 else -1
            
        