class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # original n range + without the edges of n so it can be cyclic
        new = [i for i in range(1, n+1)] + [i for i in range(n-1,1,-1)]

        while time > n:
            time -= n

        for num in new:
            if time >= 0:
                curr = num
                time -= 1

        return curr



