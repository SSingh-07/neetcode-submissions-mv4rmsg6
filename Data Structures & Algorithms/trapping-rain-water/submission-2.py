class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        maxleft = height[l]
        maxright = height[r]
        vol = 0

        while l<r:
            if maxleft < maxright:
                l+=1
                maxleft = max(maxleft, height[l])
                vol+=(maxleft - height[l])
                
            else:
                r-=1
                maxright = max(maxright, height[r])
                vol+=(maxright - height[r])
                
        return vol









        