class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        d = defaultdict(int)

        for i in range(30):
            value = 2 ** i
            store = "".join(sorted(str(value)))
            d[store] = 1
            
            orig = "".join(sorted(str(n)))

            if d[orig]:
                return True
        return False