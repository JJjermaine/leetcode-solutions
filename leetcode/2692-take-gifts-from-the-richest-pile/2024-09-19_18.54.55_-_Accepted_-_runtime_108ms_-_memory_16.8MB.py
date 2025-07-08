import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        timer = 1
        while timer <= k:
            index = gifts.index(max(gifts))

            gifts[index] = math.floor(math.sqrt(gifts[index]))
            timer += 1

        return sum(gifts)