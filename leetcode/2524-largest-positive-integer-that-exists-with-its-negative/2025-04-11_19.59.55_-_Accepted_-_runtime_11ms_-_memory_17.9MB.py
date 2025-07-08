class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        found = set()
        largest = -1
        for num in nums:
            if num < 0:
                found.add(-1 * num)
            elif num in found:
                largest = max(largest, num)
        return largest
        