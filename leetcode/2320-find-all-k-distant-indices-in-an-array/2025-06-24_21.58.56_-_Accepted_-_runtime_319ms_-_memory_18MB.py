class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        idx = []
        res = set()

        for i in range(n):
            if nums[i] == key:
                for j in range(i-k, i+k+1):
                    if j >= 0 and j < n and j not in res:
                        res.add(j)
        return list(res)
