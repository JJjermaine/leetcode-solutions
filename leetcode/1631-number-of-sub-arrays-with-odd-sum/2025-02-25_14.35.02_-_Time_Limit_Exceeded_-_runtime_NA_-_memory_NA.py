class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        subarr = []

        # generate all subarrays
        for start in range(len(arr)):
            for end in range(start, len(arr)):
                subarr.append(arr[start:end + 1])  # Extract subarray
          
        for i in range(len(subarr)):
            curr = sum(subarr[i])

            if curr % 2 != 0:
                res += 1
        return res

        