class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        negs = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                negs += 1

            if nums[i] > 0:
                if k > negs:
                    k -= negs
                    k %= negs
                else:

                break

        