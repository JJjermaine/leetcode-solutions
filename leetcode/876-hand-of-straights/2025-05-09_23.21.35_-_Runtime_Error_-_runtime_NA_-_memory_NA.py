class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        groupSize = 3
        hand.sort()
        d = Counter(hand)

        group = 0
        while True:
            if len(d) == 1 and group == groupSize-1:
                break
            if group == groupSize:
                group = 0
            # get top of dictionary
            if not d[next(iter(d)) + group]:
                return False
            d[next(iter(d))] -= 1
            if d[next(iter(d))] == 0:
                del d[next(iter(d))]


            group += 1
        return True
