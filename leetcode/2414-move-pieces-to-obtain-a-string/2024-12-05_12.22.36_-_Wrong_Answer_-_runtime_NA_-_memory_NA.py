class Solution:
    def canChange(self, start: str, target: str) -> bool:
        sp = tp = len(start)-1 # start pointer and target pointer
        while sp > 0:
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

            
            
                

        