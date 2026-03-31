class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        track = [[]]*len(position)
        for i, j in enumerate(position):
            track[i] = [j, speed[i]]

        track.sort()
        stack = []
        for [p, s] in track[::-1]:
            stack.append([p,s])
            if len(stack) >= 2:
                if (target - stack[-1][0])/ stack[-1][1] <= (target - stack[-2][0])/ stack[-2][1]:
                    stack.pop()
        return len(stack)


        