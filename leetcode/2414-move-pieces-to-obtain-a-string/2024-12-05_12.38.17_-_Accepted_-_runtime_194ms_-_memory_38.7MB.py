class Solution:
    def canChange(self, start: str, target: str) -> bool:
       # Remove underscores and compare the sequence of characters
        start_positions = [(c, i) for i, c in enumerate(start) if c != '_']
        target_positions = [(c, i) for i, c in enumerate(target) if c != '_']

        # If the sequences don't match in type or count, return False
        if len(start_positions) != len(target_positions):
            return False
        
        for (sc, si), (tc, ti) in zip(start_positions, target_positions):
            # Check if the characters match
            if sc != tc:
                return False
            
            # Ensure 'L' doesn't move to the right and 'R' doesn't move to the left
            if sc == 'L' and si < ti:
                return False
            if sc == 'R' and si > ti:
                return False
        
        return True

            
            
                

        