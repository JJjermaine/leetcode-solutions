class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        res = 0
        cost.sort()
        skip = 0
        for i in range(len(cost)-1,-1,-1):
            if skip == 2:
                skip = 0
                continue
            res += cost[i]
            skip += 1
        return res

        