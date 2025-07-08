class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(perm):
            # base case
            if len(perm) == len(nums):
                res.append(perm)  
                return

            for num in nums:
                if num not in perm:
                    backtrack(perm + [num])
                    
        backtrack([])
        return res