class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for row in mat:
            for num in range(len(row)):
                if row[num] != row[(num + k) % len(row)]:
                    return False

        return True
        