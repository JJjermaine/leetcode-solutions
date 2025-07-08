class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        subarr = []

        # generate all subarrays
        for start in range(len(arr)):
            for end in range(start, len(arr)):
                curr = sum(arr[start:end + 1])  # Extract subarray
                if curr % 2 != 0:
                    res += 1

        return res

        