class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # people with k == 0 are usually in front

        # looked at sol

        people.sort(key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res