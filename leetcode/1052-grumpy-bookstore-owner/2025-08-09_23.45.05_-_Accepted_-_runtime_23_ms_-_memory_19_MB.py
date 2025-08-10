class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # sliding window problem
        currently_satisfied = 0
        n = len(customers)
        for i in range(n):
            if grumpy[i] == 0:
                currently_satisfied += customers[i]

        l = 0
        max_satisfied = 0
        for r in range(n):
            if r >= minutes:
                if grumpy[l] == 1:
                    currently_satisfied -= customers[l]
                l += 1

            if grumpy[r] == 1:
                currently_satisfied += customers[r]

            max_satisfied = max(currently_satisfied, max_satisfied)

        return max_satisfied