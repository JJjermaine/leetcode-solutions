class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # only check locked? because all other can be changed
        # s =      "))()))""
        # locked = "010100"
        #           ^^

        stack = []
        spare = 0
        n = len(s) # or len locked
        if n % 2 != 0:
            return False
        for i in range(n):
            # if locked, cant change so if more ) than ( then it has to be false?
            if locked[i] == "1":
                if s[i] == "(": 
                    stack.append("(")
                else: 
                    if not stack and spare == 0:
                        return False
                    # while we have opening brackets or spare to close, use
                    else:
                        if stack:
                            stack.pop()
                        else:
                            spare -= 1
            # if not locked, can be either ( or )
            else:
                spare += 1
        
        if len(stack) > spare:
            return False

        return (len(stack) - spare) % 2 == 0


            
