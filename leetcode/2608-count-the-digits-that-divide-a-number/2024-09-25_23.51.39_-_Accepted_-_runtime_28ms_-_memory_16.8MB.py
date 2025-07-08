class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        string = str(num)
        for char in string:
            if int(char) != 0: # cant divide by 0
                no_decimals = ((num / int(char)).is_integer())
                if no_decimals:
                    count += 1
        return count
        