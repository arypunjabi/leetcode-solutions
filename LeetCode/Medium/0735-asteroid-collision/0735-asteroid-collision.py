from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        monoStack = deque()

        for i in range(len(asteroids)):
            asteroid = asteroids[i]
            while monoStack and monoStack[-1] > 0 and asteroid < 0 and (monoStack[-1] < (asteroid * -1)):
                monoStack.pop()
            if monoStack and monoStack[-1] > 0 and asteroid < 0 and (monoStack[-1] == (asteroid * -1)):
                monoStack.pop()
            elif monoStack and monoStack[-1] > 0 and asteroid < 0 and (monoStack[-1] > (asteroid * -1)):
                pass
            else:
                monoStack.append(asteroid)
        
        return list(monoStack)
