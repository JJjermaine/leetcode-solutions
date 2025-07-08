class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        n = len(plants)
        res = 0
        for i in range(n):
            if plants[i] > cap:
                cap = capacity
                res += (i) * 2    
            cap -= plants[i]
            res += 1
        return res