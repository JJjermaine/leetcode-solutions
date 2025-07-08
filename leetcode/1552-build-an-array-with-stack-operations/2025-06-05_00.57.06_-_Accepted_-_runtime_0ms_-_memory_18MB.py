class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        incr = 1
        for i in range(n):
            while target[i] != incr:
                res.append("Push")
                res.append("Pop")
                incr += 1

            if target[i] == incr:
                res.append("Push")
                if i == len(target) - 1:
                    break
                incr += 1
        return res
