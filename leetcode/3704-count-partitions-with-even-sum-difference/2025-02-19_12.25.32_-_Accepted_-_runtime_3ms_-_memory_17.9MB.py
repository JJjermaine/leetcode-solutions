class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            leftSum = sum(nums[:i])
            rightSum = sum(nums[i:])
            if (leftSum - rightSum) % 2 == 0:
                count += 1
        return count
        