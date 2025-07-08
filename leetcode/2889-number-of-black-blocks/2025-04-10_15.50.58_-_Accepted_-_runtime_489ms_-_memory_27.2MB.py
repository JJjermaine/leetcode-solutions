class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # Dictionary to count black cells in each 2x2 block
        block_count = defaultdict(int)

        for x, y in coordinates:
            # A black cell can affect up to 4 different 2x2 blocks
            for dx in [0, -1]:
                for dy in [0, -1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m - 1 and 0 <= ny < n - 1:
                        block_count[(nx, ny)] += 1

        # Initialize result: arr[i] = count of blocks with i black cells
        result = [0] * 5
        for count in block_count.values():
            result[count] += 1

        total_blocks = (m - 1) * (n - 1)
        result[0] = total_blocks - sum(result[1:])  # Remaining are blocks with 0 black cells

        return result

        