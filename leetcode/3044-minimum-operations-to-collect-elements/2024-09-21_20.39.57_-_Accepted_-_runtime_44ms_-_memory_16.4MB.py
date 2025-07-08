class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = set()
        #match = set(i for i in range(1, k+1))
        operations = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] >= 1 and nums[i] <= k:
                count.add(nums[i])
            operations += 1
            
            if len(count) == k:
                return operations
