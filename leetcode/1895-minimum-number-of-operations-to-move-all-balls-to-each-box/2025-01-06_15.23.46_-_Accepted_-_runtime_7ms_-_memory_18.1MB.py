class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # n^2 naive solution attempt (works but slow)
        """
        res = []
        for i in range(len(boxes)):
            operations = 0
            for j in range(len(boxes)):
                if j == i: continue
                if boxes[j] == "1": operations += abs(j - i)
            res.append(operations)
        return res
        """

        n = len(boxes)
        res = [0] * n
        
        # Pass 1: Calculate prefix sums
        count = 0  # Number of '1's encountered so far
        operations = 0  # Total operations for prefix
        for i in range(n):
            res[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count
        
        # Pass 2: Calculate postfix sums
        count = 0  # Reset the count for '1's
        operations = 0  # Reset operations for postfix
        for i in range(n - 1, -1, -1):
            res[i] += operations
            if boxes[i] == '1':
                count += 1
            operations += count
        
        return res



        