class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        curr = maxx = 0

        while l< r:
            if heights[l] < heights[r]:
                curr = heights[l]*(r-l)
                l+=1
            else:
                curr = heights[r]*(r-l)
                r-=1

            maxx = max(maxx, curr)

        return maxx

        