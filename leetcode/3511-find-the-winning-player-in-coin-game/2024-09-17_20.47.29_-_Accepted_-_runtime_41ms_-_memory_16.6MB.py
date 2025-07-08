class Solution:
    def losingPlayer(self, x: int, y: int) -> str:

        players_turn = 1 # odd represents alice currently playing, even represents bob currently playing

        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            players_turn += 1

        inDebt = x < 0 and y < 0

        if players_turn % 2 == 0 and inDebt: # if ends in alice and in debt, bob wins
            return("Bob")

        elif players_turn % 2 == 0 and not inDebt: # if ends in alice and not in debt, alice wins
            return("Alice")

        elif players_turn % 2 != 0 and inDebt: # if ends in bob and in debt, alice wins
            return("Alice")

        elif players_turn % 2 != 0 and not inDebt: # if ends in bob and not in debt, bob wins
            return("Bob")

        

        