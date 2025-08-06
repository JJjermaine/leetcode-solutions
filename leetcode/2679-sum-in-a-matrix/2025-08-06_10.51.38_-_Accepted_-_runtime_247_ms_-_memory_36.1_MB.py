class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # brute force probably doesnt work
        # we want o(n) and not o(n * m)
        for i in range(len(nums)):
            nums[i].sort()

        res = 0
        for i in range(len(nums[0])):
            curr = 0
            for j in range(len(nums)):
                print(nums[j][i])
                curr = max(curr, nums[j][i])
            res += curr
            
        return res