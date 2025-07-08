class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        current_winner = skills[0]
        winner_index = 0
        win_count = 0

        if k >= len(skills):
            for i in range(1, len(skills)):
                if skills[i] > skills[winner_index]:
                    winner_index = i

            return winner_index


        for i in range(1, len(skills)):
            if current_winner > skills[i]:
                win_count += 1
            else:
                current_winner = skills[i]
                winner_index = i
                win_count = 1

            if win_count == k:
                return winner_index

        

        
        return winner_index