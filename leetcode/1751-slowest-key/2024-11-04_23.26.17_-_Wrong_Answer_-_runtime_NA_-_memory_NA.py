class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_num = releaseTimes[0]
        res = keysPressed

        for i in range(1, len(releaseTimes)):
            curr = releaseTimes[i] - releaseTimes[i-1]

            if curr > max_num:
                max_num = curr
                res = keysPressed[i]
            elif curr >= max_num and keysPressed[i] > res:
                res = keysPressed[i]
                
        return res

            


        