class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1:
            return 0  # only one bag, so max score = min score
        
        base = weights[0] + weights[-1]
        # Calculate the cost contribution (gap) for each potential partition between i and i+1
        gaps = [weights[i] + weights[i+1] for i in range(n-1)]
        gaps.sort()
        
        # For minimum score, choose the k-1 smallest gaps
        minScore = base + sum(gaps[:k-1])
        # For maximum score, choose the k-1 largest gaps
        maxScore = base + sum(gaps[-(k-1):])
        
        return maxScore - minScore


        