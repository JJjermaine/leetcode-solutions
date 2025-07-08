class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(m):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / m)
            if stores <= n:
                return True
            else:
                return False
        

        l = 1
        r = max(quantities)
        res = 0

        while l <= r:
            m = l + (r - l) // 2
            if can_distribute(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
