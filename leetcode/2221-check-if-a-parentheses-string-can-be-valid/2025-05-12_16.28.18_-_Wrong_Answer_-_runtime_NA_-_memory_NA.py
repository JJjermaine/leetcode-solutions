class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        # Pass 1: left to right � don't allow too many ')'
        open_count = 0
        spare = 0
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    open_count += 1
                else:
                    if open_count > 0:
                        open_count -= 1
                    elif spare > 0:
                        spare -= 1  # use spare as '('
                    else:
                        return False
            else:
                spare += 1
                open_count += 1  # optimistically treat as '('

        # Pass 2: right to left � don't allow too many '('
        close_count = 0
        spare = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    close_count += 1
                else:
                    if close_count > 0:
                        close_count -= 1
                    elif spare > 0:
                        spare -= 1  # use spare as ')'
                    else:
                        return False
            else:
                spare += 1
                close_count += 1  # optimistically treat as ')'

        return True
            
