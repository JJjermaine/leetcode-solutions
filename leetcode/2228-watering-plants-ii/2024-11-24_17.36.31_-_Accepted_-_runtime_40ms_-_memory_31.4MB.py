class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l = 0
        r = len(plants) - 1
        if len(plants) == 1:
            return 0

        refill = 0
        currA = capacityA
        currB = capacityB
        while l <= r:
            if l == r: # case when theyre both in middle
                if currA >= currB:
                    if currA < plants[l]:
                        refill += 1
                    break
                else:
                    if currB < plants[r]:
                        refill += 1
                    break
            else: # regular case where Alice on left and Bob on right
                if currA < plants[l]:
                    currA = capacityA
                    refill += 1
                currA -= plants[l]
                l += 1

                if currB < plants[r]:
                    currB = capacityB
                    refill += 1
                currB -= plants[r]
                r -= 1
        return refill

            