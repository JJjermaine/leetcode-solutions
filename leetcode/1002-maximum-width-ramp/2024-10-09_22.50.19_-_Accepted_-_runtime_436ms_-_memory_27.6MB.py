class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # ans not my own

        val_index = [(val, index) for index, val in enumerate(nums)]

        val_index.sort()
        imin = float('Inf')
        res = 0
        for val, index in val_index:
            res = max(res, index - imin)
            imin = min(imin, index)

        return res
        