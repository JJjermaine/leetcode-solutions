class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # had to look at sol
        n = len(nums)
        arr = [0] * n
        
        for i in range(len(queries)):
            l, r = queries[i]
            arr[l] += 1
            if r != n-1:
                arr[r+1] -= 1

        curr = 0
        for i in range(n):
            curr += arr[i]
            if curr < nums[i]:
                return False
        return True