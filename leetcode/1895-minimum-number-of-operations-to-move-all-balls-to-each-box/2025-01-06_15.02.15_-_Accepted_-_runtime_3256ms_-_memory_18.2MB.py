class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # n^2 naive solution attempt
        res = []
        for i in range(len(boxes)):
            operations = 0
            for j in range(len(boxes)):
                if j == i: continue
                if boxes[j] == "1": operations += abs(j - i)
            res.append(operations)
        return res

        