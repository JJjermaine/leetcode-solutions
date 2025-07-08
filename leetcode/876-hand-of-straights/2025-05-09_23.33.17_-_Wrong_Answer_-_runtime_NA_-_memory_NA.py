class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        d = Counter(hand)

        while d:
            first = next(iter(d))
            for i in range(groupSize):
                if not d[first+i]:
                    return False
                d[first+i] -= 1
                if d[first+i] == 0:
                    del d[first+i]

        return True