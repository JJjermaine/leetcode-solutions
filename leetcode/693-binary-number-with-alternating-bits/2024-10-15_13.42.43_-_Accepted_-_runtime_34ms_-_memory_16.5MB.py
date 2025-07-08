class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        string_value = str(bin(n)[2:])
        for i in range(1, len(string_value)):
            if string_value[i-1] == string_value[i]:
                return False

        return True
        