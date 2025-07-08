class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # champion is the highest parent of a dag
        # if there are more than one highest parent, return -1
        champs = [True] * n
        for winner, loser in edges:
            champs[loser] = False
        
        amount_of_champs = 0
        for i in range(len(edges)):
            if champs[i]:
                amount_of_champs += 1
                champion = i
        
        if amount_of_champs > 1:
            return -1
        return champion

        