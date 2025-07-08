class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        res = [-1.0] * len(cars)  # Initialize the result with -1.0 (no collision)
        stack = []  # Stack to store the index of cars
        cars.sort(reverse=True)

        
        for i in range(len(cars)):
            pos, speed = cars[i]
            
            # Process cars in front to check when this car collides with them
            while stack:
                j = stack[-1]  # Get the car in front
                pos_j, speed_j = cars[j]
                
                # If this car cannot collide with the next one, break
                if speed <= speed_j:
                    stack.pop()
                    continue
                
                # Compute the collision time with the car in front
                time = (pos_j - pos) / (speed - speed_j)
                
                # If this car will collide after the car in front collides with its next car, break
                if res[j] == -1 or time <= res[j]:
                    res[i] = time
                    break
                else:
                    stack.pop()
            
            stack.append(i)
        
        return res
