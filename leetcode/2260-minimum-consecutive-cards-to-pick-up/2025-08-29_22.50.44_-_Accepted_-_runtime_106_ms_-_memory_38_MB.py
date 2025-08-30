class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # minimum subarray that has 2 of the same number
        minimum = len(cards)
        n = len(cards)
        d = defaultdict(int)

        for r in range(n):
            if d[cards[r]]:
                minimum = min(r - d[cards[r]] + 1, minimum)

            d[cards[r]] = r

        if minimum == n:
            if cards[0] == cards[-1] and n > 1:
                return minimum
            else:
                return -1

        return minimum