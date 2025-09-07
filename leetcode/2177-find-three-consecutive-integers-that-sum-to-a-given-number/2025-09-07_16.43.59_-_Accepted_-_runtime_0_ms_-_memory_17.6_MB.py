class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        first = num // 3 - 1
        second = num // 3
        third = num // 3 + 1
        if first + second + third == num:
            return [first, second, third]
        return []