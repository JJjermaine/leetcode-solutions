class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        arr = [0] * n
        
        for i in range(len(queries)):
            l, r = queries[i]
            for j in range(l, r+1):
                arr[j] += 1

        for i in range(n):
            if arr[i] < nums[i]:
                return False
        return True