class Solution:
    def kthCharacter(self, k: int) -> str:
        # sol not my own
        return chr(97 + (k - 1).bit_count() % 26)
            