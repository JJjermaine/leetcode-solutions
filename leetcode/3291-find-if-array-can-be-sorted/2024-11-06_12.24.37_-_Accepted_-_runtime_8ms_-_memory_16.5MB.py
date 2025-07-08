class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        pmax = 0
        cmin = 0
        cmax = 0
        pcount = 0
        for num in nums:
            ccount = num.bit_count()
            if pcount == ccount:
                cmin = min(cmin, num)
                cmax = max(cmax, num)
            elif cmin < pmax:
                return False
            else:
                pmax = cmax
                cmin = num
                cmax = num
                pcount = ccount
        return cmin >= pmax

        