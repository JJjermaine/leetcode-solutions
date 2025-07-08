class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        res = []
        while sum(d.values()) != 0:
            temp = []

            for k, v in d.items():
                if v != 0:
                    temp.append(k)
                    d[k] -= 1
                
            res.append(temp)
        return res