class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # check if base 2 to n-2
        for i in range(2, n-1):
            num = n
            nums = []
            while num:
                num, r = divmod(num, i)
                nums.append(str(r))
            string = ''.join(reversed(nums))
            if string != string[::-1]:
                return False
        return True
        
        