class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)

        if k > total:
            return total
        
        return total % k