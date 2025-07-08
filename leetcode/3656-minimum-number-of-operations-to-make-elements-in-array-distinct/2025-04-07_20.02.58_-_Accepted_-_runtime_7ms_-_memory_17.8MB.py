class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        i = 0

        while i < n:
            seen = set()
            has_duplicate = False
            for j in range(i, n):
                if nums[j] in seen:
                    has_duplicate = True
                    break
                seen.add(nums[j])
            
            if not has_duplicate:
                break  # all elements from i to n-1 are distinct
            
            operations += 1
            i += 3  # simulate removal of first 3 elements
        
        return operations