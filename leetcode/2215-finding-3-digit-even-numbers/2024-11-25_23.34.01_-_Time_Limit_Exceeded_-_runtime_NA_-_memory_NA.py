class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        for i in range(len(digits)):
            for j in range(len(digits)):
                for z in range(len(digits)):
                    if j != i and z != i and z != j:
                        number = str(digits[i]) + str(digits[j]) + str(digits[z])
                        if int(number) % 2 == 0 and digits[i] != 0 and int(number) not in res:
                            res.append(int(number))
        res.sort()
        return res
        