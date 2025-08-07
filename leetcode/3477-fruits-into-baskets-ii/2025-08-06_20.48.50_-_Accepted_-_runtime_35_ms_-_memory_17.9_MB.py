class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        d = defaultdict(int)
        res = len(fruits)
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j] and not d[j]:
                    res -= 1
                    d[j] += 1
                    break
        return res
