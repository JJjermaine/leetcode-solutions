class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    
        # [1,2,3,4,5 | 6,7,8,9,10] <- if even 1, 6, 2, 10, 3, 7...
        # [1,2,3,4,5 | 6,7,8,9] <- if odd 1, 9, 2, 6, 3, 8...
        # [1, 2, 3, 4| 5, 6, 7] <- 1, 7
        # scratch that, deque solution, ans not my own

        deck.sort(reverse=True)
        dq = deque()
        n = len(deck)
        dq.appendleft(deck[0])
        for i in range(1, n):
            dq.appendleft(dq.pop())
            dq.appendleft(deck[i])
        res = []
        while dq:
            res.append(dq.popleft())
        return res

        