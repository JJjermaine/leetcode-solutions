class ProductOfNumbers:

    def __init__(self):
        self.prod = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prod = [1]
        else:
            self.prod.append(self.prod[-1] * num)
        

    def getProduct(self, k: int) -> int:
        n = len(self.prod) - 1
        if k > n:
            return 0
        return self.prod[n] // self.prod[n-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)