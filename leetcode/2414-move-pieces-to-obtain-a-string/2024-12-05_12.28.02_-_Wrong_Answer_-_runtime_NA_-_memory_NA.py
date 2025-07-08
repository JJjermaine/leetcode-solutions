class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # edge case, more number of letters in one string
        count1 = 0
        for c in start:
            if c == "R" or c == "L":
                count1 += 1

        count2 = 0
        for c in target:
            if c == "R" or c == "L":
                count2 += 1
        if count1 != count2:
            return False

        sp = tp = len(start)-1 # start pointer and target pointer
        while sp > 0 and tp > 0:
            while sp > 0:
                if start[sp] == 'L' or start[sp] == 'R':
                    break
                sp -= 1
            while tp > 0 :
                if target[tp] == 'L' or target[tp] == 'R':
                    break
                tp -= 1
            if start[sp] != target[tp] or sp > tp and start[sp] == target[tp] == "R" or sp < tp and start[sp] == target[tp] == "L":
                return False

            sp -= 1
            tp -= 1
        
        return True

            
            
                

        