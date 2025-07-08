class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        higher_skill = skills[0]
        winner_index = 0

        if k >= len(skills):
            for i in range(1, len(skills)):
                if skills[i] > skills[winner_index]:
                    winner_index = i

        else:

            for i in range(1, k+1):
                if skills[i] > higher_skill:
                    higher_skill = skills[i]
                    winner_index = i

        
        return winner_index