class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()  # Use a set to avoid duplicate results
        curr = []
        used = [False] * len(tiles)  # Track used tiles

        def backtracking():
            if curr:
                res.add("".join(curr))  # Add to set to remove duplicates
            for i in range(len(tiles)):
                if used[i]:  # Skip already used tiles
                    continue
                used[i] = True
                curr.append(tiles[i])
                backtracking()
                curr.pop()  # Backtrack
                used[i] = False

        backtracking()
        return len(res)

        