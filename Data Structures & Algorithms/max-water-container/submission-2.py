class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        vol=curr = 0

        while l<r:
            curr = min(heights[l],heights[r])*(r-l)
            vol = max(vol, curr)

            if heights[l] <heights[r]:
                l+=1
            else:
                r-=1

        return vol
        