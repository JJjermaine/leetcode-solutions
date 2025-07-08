class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        d = Counter(arr)


        for k in sorted(d):
            if d[k] <= 0: # already encountered
                continue
            # edge case, if arr[i] == 0
            if k == 0:
                d[k] = 0
                continue
            if k < 0: # if arr[i] is negative, check if arr[i] // 2 exists
                if k / 2 in d: # {-2: 2, -4: 2} -> {-2: 0, -4: 0}
                    decAmount = d[k]
                    d[k] -= decAmount
                    d[k/2] -= decAmount
            if k > 0: # if arr[i] is pos, check if arr[i] * 2 exists
                if k * 2 in d: # {2: 2, 4: 2} -> {2: 0, 4: 0}
                    decAmount = d[k]
                    d[k] -= decAmount
                    d[k*2] -= decAmount
        return all(v == 0 for v in d.values())
