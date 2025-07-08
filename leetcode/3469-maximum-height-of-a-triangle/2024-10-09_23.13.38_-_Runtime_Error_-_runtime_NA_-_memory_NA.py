class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # try when blue or red at top
        
        height = 0

        #red on top first
        i = 0
        while (1):
            if i % 2 == 1:
                if red >= i:
                    red -= i
                else:
                    break

            else:
                if blue >= i:
                    blue -= i
                else:
                    break

            height += 1
            i += 1


        heigh2 = 0
        i = 0
        # blue on top
        while (1):
            if i % 2 != 1:
                if red >= i:
                    red -= i
                else:
                    break

            else:
                if blue >= i:
                    blue -= i
                else:
                    break

            height2 += 1
            i += 1

        return max(height1, height2)


        