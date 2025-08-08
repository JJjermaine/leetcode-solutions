class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        # for each responses[i], add them to set then add the set to hashmap?

        n = len(responses)
        d = defaultdict(int)
        for i in range(n):
            temp = set()
            for char in responses[i]:
                temp.add(char)

            for char in temp:
                d[char] += 1
        
        largest = 0
        res = ""
        for key, value in d.items():
            if value > largest:
                res = key
                largest = value
            if value == largest:
                res = min(key, res)
        return res
