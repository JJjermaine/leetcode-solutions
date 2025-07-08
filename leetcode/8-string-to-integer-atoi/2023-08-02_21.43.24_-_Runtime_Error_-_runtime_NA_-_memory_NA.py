class Solution:
    def myAtoi(self, s: str) -> int:
            newList = []
            for ch in s:
                if ch.isnumeric():
                    newList.append(ch)
                elif ch == "-":
                    newList.append(ch)
                elif ch == " ":
                    continue
                else:
                    break
            newNum = ''.join(map(str, newList))

            if newNum == "":
                return 0
            
            newNum = int(newNum)
            if newNum < -2147483648:
                newNum = -2147483648
            if newNum > 2147483647:
                newNum = 2147483647
            return newNum