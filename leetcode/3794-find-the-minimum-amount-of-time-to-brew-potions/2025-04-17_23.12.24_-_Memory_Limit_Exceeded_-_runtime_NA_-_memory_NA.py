class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        # Precompute prefix sums P: P[j][i] = sum of processing times for potion j up to wizard i
        P = [[0] * n for _ in range(m)]
        for j in range(m):
            running = 0
            for i in range(n):
                running += skill[i] * mana[j]
                P[j][i] = running

        # Compute start times S: S[j] = the time at which potion j begins processing on wizard 0
        S = [0] * m
        for j in range(1, m):
            max_cand = float('-inf')
            for i in range(n):
                prev_prefix = P[j - 1][i]
                prev_prefix_next = P[j][i - 1] if i > 0 else 0
                candidate = S[j - 1] + prev_prefix - prev_prefix_next
                if candidate > max_cand:
                    max_cand = candidate
            S[j] = max_cand

        # Final completion time is start of last potion + total processing time of last potion
        return S[m - 1] + P[m - 1][n - 1]
        