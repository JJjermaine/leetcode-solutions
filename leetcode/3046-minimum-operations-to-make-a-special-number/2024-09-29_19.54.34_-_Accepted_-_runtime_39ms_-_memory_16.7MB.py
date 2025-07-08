class Solution:
    def minimumOperations(self, num: str) -> int:
        # ans not my own
        # turn last two digits into 00, 25, 50, or 75 to be divisible by 25
        fivefound = False
        zerofound = False
        for i in range(len(num)-1,-1,-1):
            # if 5...0 or 0...0 or 2...5 or 7...5
            # then get len of nums - 2 - index
            if zerofound and num[i] == '0' or zerofound and num[i] == '5' or fivefound and num[i] == '2' or fivefound and num[i] == '7':
                return len(num) - 2 - i
            if num[i] == '5':
                fivefound = True
            if num[i] == '0':
                zerofound = True
        
        if zerofound:
            return len(num) -1

        return len(num)

        