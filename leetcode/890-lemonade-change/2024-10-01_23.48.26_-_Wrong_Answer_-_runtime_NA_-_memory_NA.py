class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveCount = 0
        tenCount = 0

        for bill in bills:
            if bill == 5:
                fiveCount += 1
            elif bill == 10:
                fiveCount -= 1
                tenCount += 1
            else:
                tenCount -= 1
                fiveCount -= 1

            if tenCount < 0 or fiveCount < 0:
                return False

        return True
        