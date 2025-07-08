class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        compare = list(count.values())[0]
        for key, value in count.items():
            if value != compare:
                return False
        return True


        