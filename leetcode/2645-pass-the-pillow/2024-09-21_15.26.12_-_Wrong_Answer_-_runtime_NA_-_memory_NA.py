class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # original n range + without the edges of n so it can be cyclic
         #new = [i for i in range(n)] + [i for i in range(n-1,-1,-1)]

        # better approach is to cut time down to n

        while time > n:
            time -= n

        return time + 1
