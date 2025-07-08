class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        curr = 0
        res = 0
        l = 0
        for r in range(n):
            if r+1 > k:
                curr -= arr[l]
                l += 1 

            curr += arr[r]
            if curr / k >= threshold and r+1 >= k:
                res += 1
        return res
        
        
