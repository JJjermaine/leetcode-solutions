class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            summation = 0
            for j in range(len(nums)):
                summation += abs(nums[i] - nums[j])

            res.append(summation)

        return res
        