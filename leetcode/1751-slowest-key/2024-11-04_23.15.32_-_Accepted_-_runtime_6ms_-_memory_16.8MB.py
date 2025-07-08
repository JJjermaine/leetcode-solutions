class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        largest_num = releaseTimes[0]
        res = [(keysPressed[0], releaseTimes[0])]
        for i in range(1, len(releaseTimes)):
            curr = releaseTimes[i] - releaseTimes[i-1]
            res.append((keysPressed[i], curr))
            largest_num = max(largest_num, curr)

        res.sort()
        for i in range(len(res)-1, -1, -1):
            if res[i][1] == largest_num:
                return res[i][0]


        