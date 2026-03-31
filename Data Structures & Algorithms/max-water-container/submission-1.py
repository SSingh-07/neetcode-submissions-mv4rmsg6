class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        currvol = 0
        vol = 0

        while l<r:
            currvol = min(heights[l], heights[r])*(r-l)
            vol = max(currvol, vol)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return vol
        