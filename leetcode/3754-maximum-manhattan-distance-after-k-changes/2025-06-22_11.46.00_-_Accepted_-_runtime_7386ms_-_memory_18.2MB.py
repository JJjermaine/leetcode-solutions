class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # maximize NE, NW, SE, or SW

        def manhattan(xi, xj, yi, yj):
            return abs(xi - xj) + abs(yi - yj)

        def maxmanhattan(prev1, next1, prev2, next2):
            n = len(s)
            d = {"N": [0,1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}
            position = [0, 0]

            largest = 0
            curr = 0
            for i in range(n):
                if s[i] == prev1 and curr != k: 
                    position[0] += d[next1][0]
                    position[1] += d[next1][1]
                    curr += 1
                elif s[i] == prev2 and curr !=k : 
                    position[0] += d[next2][0]
                    position[1] += d[next2][1]
                    curr += 1
                else: 
                    position[0] += d[s[i]][0]
                    position[1] += d[s[i]][1]
                largest = max(largest, manhattan(0, position[0], 0, position[1]))
            return largest

        largest = 0
        # change all S to N and W to E 
        largest = max(largest, maxmanhattan("S", "N", "W", "E"))
        # change all S to N and E to W 
        largest = max(largest, maxmanhattan("S", "N", "E", "W"))
        # change all N to S and W to E 
        largest = max(largest, maxmanhattan("N", "S", 'W', "E"))
        # change all N to S and E to W 
        largest = max(largest, maxmanhattan("N", "S", "E", "W"))
        return largest

        

        

        