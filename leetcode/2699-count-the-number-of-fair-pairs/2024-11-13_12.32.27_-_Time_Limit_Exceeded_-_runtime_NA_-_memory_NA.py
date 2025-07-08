class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = []
        for i in range(len(nums)):
            res.append((nums[i], i))
        res.sort()
        # i < j < n
        # lower <= nums[i] + nums[j] <= upper
        count = 0
        for i in range(len(res)):
            for j in range(len(res)):
                if res[i][1] < res[j][1] and lower <= (res[i][0] + res[j][0]) <= upper:
                    count += 1
        return count

        