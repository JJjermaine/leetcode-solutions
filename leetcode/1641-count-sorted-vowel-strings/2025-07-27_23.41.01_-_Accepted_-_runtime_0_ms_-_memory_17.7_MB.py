class Solution:
    def countVowelStrings(self, n: int) -> int:
        # iterating through each solution is possible because constraint is 1 to 50
        # finding the formula is math is probably faster and better
        # when [n = 1,2,3,4,5] -> ans = [5,15,35,70,126,210] -> diff in ans = [10,20,35,56,84]
        # diff in diff in ans = [10,15,21,28] -> diff in diff in diff in and = [5,6,7]

        diff_3 = 5
        diff_2 = 10
        diff_1 = 10
        res = 5

        for i in range(n-1):
            res += diff_1
            diff_1 += diff_2
            diff_2 += diff_3
            diff_3 += 1
        return res

        
