class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)

        fleet = 1
        prevtime = (target - pairs[0][0])/pairs[0][1]
        for curr in pairs[1:]:
            currtime = (target - curr[0])/curr[1]

            if currtime > prevtime:
                fleet+=1

                prevtime = currtime

        return fleet





        